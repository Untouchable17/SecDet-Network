from rest_framework import viewsets, parsers, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from src.base.services import delete_old_file
from src.base.permissions import IsAuthor
from src.posts import serializers
from src.posts import models


class ArticleView(viewsets.ModelViewSet):
    """ CRUD постов пользователя """

    parser_classes = (parsers.MultiPartParser,)
    serializer_class = serializers.ArticleSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        return models.Article.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AddPostLike(APIView):
    """ Поставить лайк на запись """

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        article = models.Article.objects.get(id=pk)

        is_dislike = False

        for dislike in article.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            article.likes.remove(request.user.id)

        is_like = False

        for like in article.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            article.likes.add(request.user.id)

        if is_like:
            article.likes.remove(request.user)

        return Response(status=201)


class AddPostDislike(APIView):
    """ Убрать лайк от записи """

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        article = models.Article.objects.get(id=pk)

        is_like = False

        for like in article.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            article.likes.remove(request.user)

        is_dislike = False

        for dislike in article.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            article.dislikes.add(request.user.id)

        if is_dislike:
            article.dislikes.remove(request.user)

        return Response(status=201)


class CommentAuthorView(viewsets.ModelViewSet):
    """ CRUD комментариев пользователя """

    serializer_class = serializers.CommentAuthorSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        return models.Comment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentView(viewsets.ModelViewSet):
    """ Все комментарии к посту """

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = serializers.CommentSerializer

    def get_queryset(self):
        return models.Comment.objects.filter(article_id=self.kwargs.get('pk'))
