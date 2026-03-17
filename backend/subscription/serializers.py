from rest_framework import serializers
from .models import SubscriptionTier, UserSubscription


class SubscriptionTierSerializer(serializers.ModelSerializer):
    """Serialize subscription tier data."""

    class Meta:
        model = SubscriptionTier
        fields = ['id', 'name', 'price', 'max_usage', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class UserSubscriptionSerializer(serializers.ModelSerializer):
    """Serialize user subscription data with tier details."""
    tier = SubscriptionTierSerializer(read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = UserSubscription
        fields = ['id', 'user_email', 'tier', 'usage_left', 'is_active', 'subscribed_at', 'updated_at']
        read_only_fields = ['subscribed_at', 'updated_at']


class SubscribeSerializer(serializers.Serializer):
    """Serialize subscription request data."""
    tier_id = serializers.IntegerField()

    def validate_tier_id(self, value):
        try:
            tier = SubscriptionTier.objects.get(id=value)
            return tier
        except SubscriptionTier.DoesNotExist:
            raise serializers.ValidationError("Subscription tier not found.")

    def validate(self, data):
        if 'tier_id' in data:
            data['tier'] = data.pop('tier_id')
        return data
