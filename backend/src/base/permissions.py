from rest_framework import permissions


class IsAuthor(permissions.IsAuthenticated):
    """ Проверка является ли пользователь создателем/автором объекта """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsGroupAdministrator(permissions.IsAuthenticated):
    """ Проверка является ли пользователь администратором группы """

    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.group.is_group_administrator)


class IsGroupModerator(permissions.IsAuthenticated):
    """ Проверка является ли пользователь модератором группы """

    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.group.is_group_moderator)


class IsGroupEditor(permissions.IsAuthenticated):
    """ Проверка является ли пользователь редактором группы """

    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.group.is_group_editor)


