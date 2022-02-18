from django.contrib import admin

from src.groups import models


@admin.register(models.Group)
class GroupCustomAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "verified", "title", "created_at")
    list_display_links = ("id", "title")


@admin.register(models.GroupArticles)
class GroupArticlesAdmin(admin.ModelAdmin):
    list_display = ("id", "group", "title", "creator", "created_at")
    list_display_links = ("id", "title",)


