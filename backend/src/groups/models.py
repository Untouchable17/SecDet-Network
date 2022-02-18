from django.core.validators import FileExtensionValidator
from django.db import models

from src.auth_system.models import UserProfile
from src.base import services


class Group(models.Model):
    """ Модель группы """

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="group_owner")
    verified = models.BooleanField(default=False, verbose_name="Верифицированная группа")
    title = models.CharField(max_length=50, verbose_name="Названия группы")
    community_image = models.ImageField(
        upload_to=services.get_path_upload_group_community_image,
        blank=True,
        default="default_user.jpg",
        validators=[FileExtensionValidator(
            allowed_extensions=['jpg', 'png']), services.validate_size_image]
    )
    background_image = models.ImageField(
        upload_to=services.get_path_upload_group_background_image,
        blank=True,
        default="default_user.jpg",
        validators=[FileExtensionValidator(
            allowed_extensions=['jpg', 'png', 'gif']), services.validate_size_image]
    )
    short_descr = models.CharField(max_length=75, blank=True, verbose_name="Короткое описание")
    description = models.TextField(max_length=5000, blank=True, verbose_name="Описание группы")
    followers = models.ManyToManyField(UserProfile, blank=True, related_name='group_followers')

    is_group_administrator = models.ManyToManyField(UserProfile, related_name="group_administrator",
                                                    verbose_name="Владелец группы")
    is_group_moderator = models.ManyToManyField(UserProfile, blank=True, related_name="group_moderator",
                                                verbose_name="Модератор группы",)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания группы")

    def __str__(self):
        return f"{self.user} - {self.title}"

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class GroupArticles(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="group_article",
                              verbose_name="Записи в группе",)
    creator = models.ForeignKey(UserProfile, on_delete=models.PROTECT,
                                related_name="group_article_creator", verbose_name="Кто создал запись")
    title = models.CharField(max_length=255, verbose_name="Заголовок записи")
    content = models.TextField(max_length=8000, verbose_name="Содержимое записи")
    image = models.ImageField(
        upload_to=services.get_path_upload_group_article_image,
        blank=True,
        default="default_user.jpg",
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png']), services.validate_size_image]
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    change_at = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")
    is_private = models.BooleanField(default=False, verbose_name="Публичный доступ")
    likes = models.ManyToManyField(UserProfile, blank=True, related_name='group_article_likes')
    dislikes = models.ManyToManyField(UserProfile, blank=True, related_name='group_article_dislikes')

    def __str__(self):
        return f"{self.group} -> {self.title}"



