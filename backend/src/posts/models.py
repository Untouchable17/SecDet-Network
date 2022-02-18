from django.core.validators import FileExtensionValidator
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.db import models

from src.auth_system.models import UserProfile
from src.base import services


class Article(models.Model):
    """ Модель поста """

    title = models.CharField(max_length=255, verbose_name="Заголовок поста")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="article_author")

    image = models.ImageField(
        upload_to=services.product_image_directory_path,
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png']), services.validate_size_image]

    )
    description = models.TextField(verbose_name="Текст поста")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    change_at = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")
    is_chart = models.BooleanField(default=False, verbose_name="Публичный доступ")
    likes = models.ManyToManyField(UserProfile, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(UserProfile, blank=True, related_name='dislikes')

    # def get_absolute_url(self):
    #     return reverse('posts:post-detail', kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.user} | {self.created_at}"

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comment(models.Model):
    """ Модель комментария к посту """

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='comments')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_comments')
    text = models.TextField(max_length=800, verbose_name="Текст комментария")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания комментария")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"