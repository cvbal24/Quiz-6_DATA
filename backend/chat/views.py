from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from subscription.models import UserSubscription
from .models import ChatHistory
from .serializers import ChatRequestSerializer, ChatResponseSerializer


class AIChatbotView(APIView):
    """AI Chatbot endpoint with subscription paywall."""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Check subscription
        try:
            subscription = UserSubscription.objects.get(user=request.user)
        except UserSubscription.DoesNotExist:
            return Response(
                {'detail': 'No active subscription. Please subscribe to use chatbot.'},
                status=status.HTTP_403_FORBIDDEN
            )

        # Check subscription is active
        if not subscription.is_active:
            return Response(
                {'detail': 'Your subscription is inactive.'},
                status=status.HTTP_403_FORBIDDEN
            )

        # Check usage remaining
        if subscription.usage_left <= 0:
            return Response(
                {'detail': 'You have reached your usage limit. Please upgrade your subscription.'},
                status=status.HTTP_403_FORBIDDEN
            )

        # Validate request
        serializer = ChatRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        message = serializer.validated_data['message']

        # Generate AI response (placeholder for now)
        # In production, integrate with OpenAI API or similar
        ai_response = f"Echo: {message}"

        # Save chat history
        chat = ChatHistory.objects.create(
            user=request.user,
            message=message,
            response=ai_response
        )

        # Decrement usage
        subscription.usage_left -= 1
        subscription.save()

        # Return response
        response_data = ChatResponseSerializer({
            'message': message,
            'response': ai_response,
            'usage_left': subscription.usage_left,
        }).data

        return Response(response_data, status=status.HTTP_200_OK)
