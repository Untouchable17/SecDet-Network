from rest_framework import serializers

from src.tracks import models
from src.base.services import delete_old_file
from src.auth_system.serializers import ProfileSerializer


class BaseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)


class GenreSerializer(BaseSerializer):
    class Meta:
        model = models.Genre
        fields = ('id', 'title')


class AlbumSerializer(BaseSerializer):
    class Meta:
        model = models.Album
        fields = ('id', 'title', 'description', 'picture', 'private')

    def update(self, instance, validated_data):
        delete_old_file(instance.picture.path)
        return super().update(instance, validated_data)


class CreateAuthorTrackSerializer(BaseSerializer):
    plays_count = serializers.IntegerField(read_only=True)
    download = serializers.IntegerField(read_only=True)
    user = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.Track
        fields = (
            'id',
            'title',
            'genre',
            'album',
            'link_of_author',
            'file',
            'created_at',
            'plays_count',
            'download',
            'private',
            'picture',
            'user'
        )

    def update(self, instance, validated_data):
        delete_old_file(instance.file.path)
        delete_old_file(instance.picture.path)
        return super().update(instance, validated_data)


class AuthorTrackSerializer(CreateAuthorTrackSerializer):
    genre = GenreSerializer(many=True)
    album = AlbumSerializer()
    user = ProfileSerializer()


class CreatePlayListSerializer(BaseSerializer):
    class Meta:
        model = models.PlayList
        fields = ('id', 'title', 'picture', 'tracks')

    def update(self, instance, validated_data):
        delete_old_file(instance.picture.path)
        return super().update(instance, validated_data)


class PlayListSerializer(CreatePlayListSerializer):
    tracks = AuthorTrackSerializer(many=True)


