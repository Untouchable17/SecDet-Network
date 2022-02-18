from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

from src.auth_system import models

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = (
            "avatar",
            "display_name",
            "country",
            "biography",
            "email"
        )


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = (
            "id",
            "email",
            "display_name",
            "password"
        )


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = (
            "avatar",
            "display_name",
            "country",
            "biography",
            "followers"
        )
