from typing import Optional
from datetime import datetime

from rest_framework import authentication, exceptions
from django.conf import settings
import jwt

from src.auth_system.models import UserProfile


class AuthBackend(authentication.BaseAuthentication):
    authentication_header_prefix = 'Token'

    def authenticate(self, request, token=None, **kwargs) -> Optional[tuple]:
        auth_header = authentication.get_authorization_header(request).split()

        if not auth_header or auth_header[0].lower() != b'token':
            return None

        if len(auth_header) == 1:
            raise exceptions.AuthenticationFailed(
                'Недопустимый заголовок токена. Учетные данные не были предоставлены!'
            )

        elif len(auth_header) > 2:
            raise exceptions.AuthenticationFailed(
                "Недопустимый заголовок токена. Строка токена не должна содержать пробелов!"
            )

        try:
            token = auth_header[1].decode('utf-8')

        except UnicodeError:
            raise exceptions.AuthenticationFailed(
                "Недопустимый заголовок токена. Строка токена не должна содержать недопустимых символов!"
            )

        return self.authenticate_credential(token)

    def authenticate_credential(self, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
        except jwt.PyJWTError:
            raise exceptions.AuthenticationFailed(
                'Неверная аутентификация. Не удалось расшифровать токен!'
            )

        token_exp = datetime.fromtimestamp(payload['exp'])

        if token_exp < datetime.utcnow():
            raise exceptions.AuthenticationFailed("Срок действия токена истек!")

        try:
            user = UserProfile.objects.get(id=payload['user_id'])
        except UserProfile.DoesNotExist():
            raise exceptions.AuthenticationFailed(
                'Пользователь, соответствующий этому токену, не был найден!'
            )

        return user, None