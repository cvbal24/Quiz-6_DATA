from rest_framework import serializers

from .models import SellerApplication


class SellerApplicationSerializer(serializers.ModelSerializer):
    user_first_name = serializers.CharField(source='user.first_name', read_only=True)
    user_last_name = serializers.CharField(source='user.last_name', read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = SellerApplication
        fields = [
            'id',
            'user',
            'user_first_name',
            'user_last_name',
            'user_email',
            'status',
            'decline_reason',
            'created_at',
        ]
        read_only_fields = ['id', 'user', 'status', 'decline_reason', 'created_at']


class ApproveApplicationSerializer(serializers.Serializer):
    merchant_id = serializers.CharField(max_length=255)


class DeclineApplicationSerializer(serializers.Serializer):
    decline_reason = serializers.CharField(allow_blank=False)
