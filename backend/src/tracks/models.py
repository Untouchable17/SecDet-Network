from django.core.validators import FileExtensionValidator
from django.db import models

from src.auth_system.models import UserProfile
from src.base import services


class Album(models.Model):
    """ Модель альбома """

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="albums")
    title = models.CharField(max_length=75, verbose_name="Заголовок альбома")
    description = models.TextField(max_length=700, verbose_name="Описание альбома")
    private = models.BooleanField(default=False, verbose_name="Приватность")
    picture = models.ImageField(
        upload_to=services.get_path_upload_picture_album,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(
            allowed_extensions=['jpg', 'png']), services.validate_size_image],
    )

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"


class Genre(models.Model):
    """ Модель жанров для треков """

    title = models.CharField(max_length=30, unique=True, verbose_name="Жанр трека")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Track(models.Model):
    """ Модель аудиофайлов """

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="tracks")
    title = models.CharField(max_length=175, verbose_name="Заголовок песни")
    genre = models.ManyToManyField(Genre, related_name="track_genres", verbose_name="Жанр(ы) песни")
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, blank=True, null=True)
    link_of_author = models.CharField(max_length=720, blank=True, null=True,
                                      verbose_name="Ссылка стороннего ресурса")
    file = models.FileField(
        upload_to=services.get_path_upload_track,
        validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav'])],
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки файла")
    plays_count = models.PositiveIntegerField(default=0, verbose_name="Количество прослушиваний песни")
    download_count = models.PositiveIntegerField(default=0, verbose_name="Количество загрузок песни")
    private = models.BooleanField(default=False, verbose_name="Общедоступный")
    picture = models.ImageField(
        upload_to=services.get_path_upload_picture_track,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(
            allowed_extensions=['jpg', 'png']), services.validate_size_image],
    )

    def __str__(self):
        return f"{self.user} -> {self.title}"

    class Meta:
        verbose_name = "Аудиофайл"
        verbose_name_plural = "Аудиофайлы"


class PlayList(models.Model):
    """ Модель плейлистов пользователя """

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="play_lists")
    title = models.CharField(max_length=75, verbose_name="Заголовок плейлиста")
    tracks = models.ManyToManyField(Track, related_name="track_playlist", verbose_name="Треки в плейлисте")
    picture = models.ImageField(
        upload_to=services.get_path_upload_picture_playlist,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png']), services.validate_size_image],
    )

    class Meta:
        verbose_name = "Плейлист"
        verbose_name_plural = "Плейлист"


