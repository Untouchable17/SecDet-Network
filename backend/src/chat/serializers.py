from rest_framework import serializers

from src.chat.models import Messages


class MessagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Messages
        fields = [
            'user_from',
            'user_to',
            'message',
            'message_created',
        ]