from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
from django.core.validators import FileExtensionValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.db import models

from src.base.services import (
    get_path_upload_avatar, validate_size_image
)

User = settings.AUTH_USER_MODEL


class UserProfile(models.Model):
    """ Модель пользователя на сайта """

    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, verbose_name='Пользователь')
    display_name = models.CharField(max_length=50, verbose_name="Отображаемое имя/никнейм")
    email = models.EmailField(max_length=175, verbose_name="Почта пользователя")
    join_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")
    country = models.CharField(max_length=30, blank=True, null=True, verbose_name="Город пользователя")
    biography = models.TextField(max_length=255, blank=True, null=True, verbose_name="Статус пользователя")
    followers = models.ManyToManyField(User, blank=True, related_name='followers')
    avatar = models.ImageField(
        upload_to=get_path_upload_avatar,
        blank=True,
        default="default_user.jpg",
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'gif']), validate_size_image]

    )

    @property
    def is_authenticated(self):
        """ Функция для проверки аутентификации """
        return True

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


class UserAccountManager(BaseUserManager):
    """ Кастомный менеджер для модели UserAccount """

    def create_user(self, email, password=None, **extra_fields):
        """ Создание обычного пользователя """

        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """ Создание суперпользователя """

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault("is_active", True)

        user = self.create_user(email=email, password=password, **extra_fields)
        user.is_admin = True

        user.save(using=self._db)

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    """ Модель для регистрации нового пользователя """

    display_name = models.CharField(max_length=50, verbose_name="Отображаемое имя/никнейм")
    email = models.EmailField(max_length=175, unique=True, verbose_name="Почта пользователя")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["display_name"]

    def get_full_name(self):
        return f"{self.display_name}"

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



