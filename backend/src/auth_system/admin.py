from django.contrib import admin

from src.auth_system import models


@admin.register(models.UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "email")


@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "email", "join_date")
    list_display_links = ("id", "email", )