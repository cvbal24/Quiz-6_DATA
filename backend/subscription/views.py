from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import SubscriptionTier, UserSubscription
from .serializers import (
    SubscriptionTierSerializer,
    UserSubscriptionSerializer,
    SubscribeSerializer,
)
from users.permissions import IsAdminRole


class ListTiersView(ListAPIView):
    """List all available subscription tiers."""
    queryset = SubscriptionTier.objects.all()
    serializer_class = SubscriptionTierSerializer
    permission_classes = []


class SubscribeView(APIView):
    """Subscribe user to a subscription tier."""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = SubscribeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            tier = serializer.validated_data['tier']
            user_subscription, created = UserSubscription.objects.get_or_create(
                user=request.user,
                defaults={
                    'tier': tier,
                    'usage_left': tier.max_usage,
                    'is_active': True,
                }
            )
            if not created:
                # Update existing subscription
                user_subscription.tier = tier
                user_subscription.usage_left = tier.max_usage
                user_subscription.is_active = True
                user_subscription.save()
            return Response(
                UserSubscriptionSerializer(user_subscription).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CurrentSubscriptionView(APIView):
    """Get current user's subscription details."""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            subscription = UserSubscription.objects.get(user=request.user)
            serializer = UserSubscriptionSerializer(subscription)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserSubscription.DoesNotExist:
            return Response(
                {'detail': 'No active subscription found.'},
                status=status.HTTP_404_NOT_FOUND
            )


class AdminSubscriptionListView(ListAPIView):
    """Admin view: list all user subscriptions."""
    queryset = UserSubscription.objects.select_related('user', 'tier').all()
    serializer_class = UserSubscriptionSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]
