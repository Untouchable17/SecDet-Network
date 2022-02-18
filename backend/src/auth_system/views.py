from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from src.base.services import delete_old_file
from src.base.permissions import IsAuthor
from src.auth_system import serializers
from src.auth_system import models


class ProfileView(APIView):
    """ Просмотр профиля """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        profile = models.UserProfile.objects.get(id=pk)
        serializer = serializers.UserSerializer(profile)

        return Response(serializer.data)


class ProfileEdit(APIView):
    """ Редактирование профиля """

    permission_classes = [IsAuthor]

    def put(self, request, pk):
        serializer = serializers.UserSerializer(
            data=request.data, instance=request.user
        )
        if serializer.is_valid():
            serializer.save()
        return Response(status=201)


class AddFollower(APIView):
    """ Подписаться на пользователя """

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        profile = models.UserProfile.objects.get(id=pk)
        profile.followers.add(request.user.id)

        return Response(status=201)


class RemoveFollower(APIView):
    """ Отписаться от пользователя"""

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        profile = models.UserProfile.objects.get(id=pk)
        profile.followers.remove(request.user.id)

        return Response(status=201)




