from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.permissions import IsAdminRole

from .models import Service
from .serializers import ServiceManageSerializer, ServiceSerializer


class ListServicesView(generics.ListAPIView):
    queryset = Service.objects.select_related('seller').all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]


class ServiceDetailView(generics.RetrieveAPIView):
    queryset = Service.objects.select_related('seller')
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]


class SellerCreateServiceView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # Only sellers can create services
        user = request.user
        if user.role != 'Seller':
            return Response(
                {'detail': 'Only sellers can create services.'},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = ServiceManageSerializer(data=request.data)
        if serializer.is_valid():
            service = serializer.save(seller=user)
            return Response(
                ServiceSerializer(service).data,
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SellerManageServiceView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk, user):
        try:
            service = Service.objects.get(pk=pk, seller=user)
            return service
        except Service.DoesNotExist:
            return None

    def patch(self, request, pk):
        user = request.user
        service = self.get_object(pk, user)

        if not service:
            return Response(
                {'detail': 'Service not found or you do not have permission to edit it.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = ServiceManageSerializer(service, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(ServiceSerializer(service).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        user = request.user
        service = self.get_object(pk, user)

        if not service:
            return Response(
                {'detail': 'Service not found or you do not have permission to edit it.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = ServiceManageSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(ServiceSerializer(service).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = request.user
        try:
            service = Service.objects.get(pk=pk, seller=user)
        except Service.DoesNotExist:
            return Response(
                {'detail': 'Service not found or you do not have permission to delete it.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        service.delete()
        return Response({'detail': 'Service deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
