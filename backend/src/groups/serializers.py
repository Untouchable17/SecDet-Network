from rest_framework import serializers

from src.groups import models


class GroupCustomSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Group
        fields = [
            "user",
            "verified",
            "title",
            "community_image",
            "background_image",
            "short_descr",
            "description",
            "followers",
            "is_group_administrator",
            "is_group_moderator"
        ]


class GroupArticlesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.GroupArticles
        fields = [
            "group",
            "creator",
            "title",
            "content",
            "image",
            "change_at",
            "likes",
            "dislikes"
        ]


