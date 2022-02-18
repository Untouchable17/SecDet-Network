import os

from django.http import FileResponse, Http404, HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets, parsers, permissions
from rest_framework.views import APIView

from src.base.classes import MixedSerializer, Pagination
from src.tracks import serializers, models
from src.base.permissions import IsAuthor
from src.base.services import delete_old_file


class GenreView(generics.ListAPIView):
    """ Список жанров """

    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer


class AlbumView(viewsets.ModelViewSet):
    """ CRUD альбомов пользователя """

    parser_classes = (parsers.MultiPartParser,)
    serializer_class = serializers.AlbumSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        return models.Album.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        delete_old_file(instance.picture.path)
        instance.delete()


class PublicAlbumView(generics.ListAPIView):
    """ Общедоступные альбомы пользователя """

    serializer_class = serializers.AlbumSerializer

    def get_queryset(self):
        return models.Album.objects.filter(
            user__id=self.kwargs.get('pk'), private=False
        )


class TrackView(MixedSerializer, viewsets.ModelViewSet):
    """ CRUD для аудиофайлов """

    parser_classes = (parsers.MultiPartParser,)
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = serializers.CreateAuthorTrackSerializer
    serializer_classes_by_action = {
        'list': serializers.AuthorTrackSerializer
    }

    def get_queryset(self):
        return models.Track.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        delete_old_file(instance.picture.path)
        delete_old_file(instance.file.path)
        instance.delete()


class PlayListView(MixedSerializer, viewsets.ModelViewSet):
    """ CRUD для плейлистов """

    parser_classes = (parsers.MultiPartParser,)
    permission_classes = [IsAuthor]

    serializer_class = serializers.CreatePlayListSerializer
    serializer_classes_by_action = {
        'list': serializers.PlayListSerializer
    }

    def get_queryset(self):
        return models.PlayList.objects.filter(
            user=self.request.user.profile
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.profile)

    def perform_destroy(self, instance):
        delete_old_file(instance.picture.path)
        instance.delete()


class TrackListView(generics.ListAPIView):
    """ Выводит список всех аудиофайлов """

    queryset = models.Track.objects.filter(
        album__private=False, private=False
    )
    serializer_class = serializers.AuthorTrackSerializer
    pagination_class = Pagination


class AuthorTrackListView(generics.ListAPIView):
    """ Список всех аудиофайлов пользователя """

    serializer_class = serializers.AuthorTrackSerializer
    pagination_class = Pagination

    def get_queryset(self):
        return models.Track.objects.filter(
            user__id=self.kwargs.get('pk'), album__private=False, private=False
        )


class StreamingFileView(APIView):
    """ Прослушивание аудиофайла """

    def set_play(self, track):
        track.plays_count += 1
        track.save()

    def get(self, request, pk):
        track = get_object_or_404(models.Track, id=pk)
        if os.path.exists(track.file.path):
            self.set_play(track)
            return FileResponse(open(track.file.path, 'rb'), filename=track.file.name)
        else:
            return Http404


class DownloadTrackView(APIView):
    """ Скачивание аудиофайла """

    def set_download(self):
        self.track.download_count += 1
        self.track.save()

    def get(self, request, pk):
        self.track = get_object_or_404(models.Track, id=pk)
        if os.path.exists(self.track.file.path):
            self.set_download()
            return FileResponse(open(
                self.track.file.path, 'rb'),
                filename=self.track.file.name,
                as_attachment=True
            )
        else:
            return Http404

