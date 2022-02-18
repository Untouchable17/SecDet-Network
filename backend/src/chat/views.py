from rest_framework import viewsets

from src.base.permissions import IsAuthor
from src.chat.models import Messages
from src.chat import serializers


class GetMessages(viewsets.ModelViewSet):

    permission_classes = [IsAuthor]
    serializer_class = serializers.MessagesSerializer

    def get_queryset(self):
        return Messages.objects.filter(
            user_from=self.request.user.id, user_to=self.kwargs.get('pk')
        )

    def perform_create(self, serializer):
        serializer.save(user_from=self.request.user)

