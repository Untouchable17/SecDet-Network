from rest_framework import viewsets, parsers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from src.groups.models import Group, GroupArticles
from src.groups import serializers


class ShowFollowerGroups(viewsets.ModelViewSet):
    """ Возвращает список групп, на которые подписан пользователь """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.GroupCustomSerializer

    def get_queryset(self):
        return Group.objects.filter(followers=self.request.user)


class GroupsView(viewsets.ModelViewSet):
    """ CRUD для групп (только для администратора группы) """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.GroupCustomSerializer

    def get_queryset(self):
        return Group.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AddGroupFollower(APIView):
    """ Подписаться на группу """

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        group = Group.objects.get(id=pk)
        group.followers.add(request.user.id)

        return Response(status=201)


class RemoveGroupFollower(APIView):
    """ Отписаться от группы """

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        group = Group.objects.get(id=pk)
        group.followers.remove(request.user.id)

        return Response(status=201)


class GroupArticleView(viewsets.ModelViewSet):
    """ CRUD для записей в группе (администратор/модератор) """

    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (parsers.MultiPartParser,)
    serializer_class = serializers.GroupArticlesSerializer

    def get_queryset(self):
        return GroupArticles.objects.filter(group_id=self.kwargs.get('pk'))

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


