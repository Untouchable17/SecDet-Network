from django.contrib.auth import get_user_model
from rest_framework import serializers

from src.auth_system.serializers import ProfileSerializer
from src.posts import models

User = get_user_model()


class ArticleSerializer(serializers.ModelSerializer):
    """ Сериализация поста """

    class Meta:
        model = models.Article
        fields = (
            "id",
            "title",
            "description",
            "image",
            "likes",
            "dislikes",
        )


class CommentAuthorSerializer(serializers.ModelSerializer):
    """ Сериализация комментариев конкретного пользователя """

    class Meta:
        model = models.Comment
        fields = ('id', 'text', 'article')


class CommentSerializer(serializers.ModelSerializer):
    """ Сериализация всех комментариев к посту """

    user = ProfileSerializer()

    class Meta:
        model = models.Comment
        fields = ('id', 'text', 'user', 'article', 'created_at')

