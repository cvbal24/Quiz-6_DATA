from rest_framework import serializers
from .models import ChatHistory


class ChatRequestSerializer(serializers.Serializer):
    """Serialize incoming chat request."""
    message = serializers.CharField(max_length=2000, min_length=1)


class ChatResponseSerializer(serializers.Serializer):
    """Serialize outgoing chat response with usage info."""
    message = serializers.CharField()
    response = serializers.CharField()
    usage_left = serializers.IntegerField()


class ChatHistorySerializer(serializers.ModelSerializer):
    """Serialize chat history for retrieval."""
    user_email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = ChatHistory
        fields = ['id', 'user_email', 'message', 'response', 'created_at']
        read_only_fields = ['created_at']
