from django.utils import timezone
from django.db import models

from src.auth_system.models import UserProfile


class Messages(models.Model):
    """ Модель сообщений """

    user_from = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="+")
    user_to = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="+")
    message = models.TextField(verbose_name="Текст сообщения")
    message_created = models.DateTimeField(default=timezone.now, verbose_name="Дата сообщения")

    def __str__(self):
        return f"{self.user_from} - {self.message}"