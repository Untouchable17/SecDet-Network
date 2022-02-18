from django.contrib import admin

from src.tracks import models


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("title",)


@admin.register(models.Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "title")
    list_display_links = ("user", )
    list_filter = ("user", )


@admin.register(models.Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "title", "created_at")
    list_display_links = ("user", )
    list_filter = ("genre", "created_at")
    search_fields = ("user__email", "user__display_name", "genre__name"),


@admin.register(models.PlayList)
class PlayListAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "title")
    list_display_links = ("user", )
    search_fields = ("user__email", "user__display_name", "tracks__title"),
