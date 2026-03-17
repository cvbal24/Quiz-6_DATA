from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from services.models import Service

from .models import Order
from .serializers import OrderCreateSerializer, OrderSerializer


class CreateOrderView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = OrderCreateSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save(buyer=request.user)
            return Response(
                OrderSerializer(order).data,
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderHistoryView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(buyer=self.request.user).select_related('service', 'buyer')
