from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import CustomUser
from users.permissions import IsAdminRole

from .models import SellerApplication
from .serializers import (
	ApproveApplicationSerializer,
	DeclineApplicationSerializer,
	SellerApplicationSerializer,
)


class SubmitApplicationView(APIView):
	permission_classes = [permissions.IsAuthenticated]

	def post(self, request):
		application, created = SellerApplication.objects.get_or_create(
			user=request.user,
			defaults={'status': SellerApplication.Status.PENDING},
		)

		if not created:
			if application.status == SellerApplication.Status.PENDING:
				return Response({'detail': 'Application already submitted and pending.'}, status=status.HTTP_400_BAD_REQUEST)
			application.status = SellerApplication.Status.PENDING
			application.decline_reason = ''
			application.save(update_fields=['status', 'decline_reason'])

		serializer = SellerApplicationSerializer(application)
		return Response(serializer.data, status=status.HTTP_201_CREATED)


class ListApplicationsView(generics.ListAPIView):
	queryset = SellerApplication.objects.select_related('user').order_by('-created_at')
	serializer_class = SellerApplicationSerializer
	permission_classes = [IsAdminRole]


class ApproveApplicationView(APIView):
	permission_classes = [IsAdminRole]

	def post(self, request, pk):
		serializer = ApproveApplicationSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)

		application = SellerApplication.objects.select_related('user').filter(pk=pk).first()
		if not application:
			return Response({'detail': 'Application not found.'}, status=status.HTTP_404_NOT_FOUND)

		application.status = SellerApplication.Status.APPROVED
		application.decline_reason = ''
		application.save(update_fields=['status', 'decline_reason'])

		user = application.user
		user.role = CustomUser.Role.SELLER
		user.merchant_id = serializer.validated_data['merchant_id']
		user.save(update_fields=['role', 'merchant_id'])

		return Response(SellerApplicationSerializer(application).data, status=status.HTTP_200_OK)


class DeclineApplicationView(APIView):
	permission_classes = [IsAdminRole]

	def post(self, request, pk):
		serializer = DeclineApplicationSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)

		application = SellerApplication.objects.select_related('user').filter(pk=pk).first()
		if not application:
			return Response({'detail': 'Application not found.'}, status=status.HTTP_404_NOT_FOUND)

		application.status = SellerApplication.Status.DECLINED
		application.decline_reason = serializer.validated_data['decline_reason']
		application.save(update_fields=['status', 'decline_reason'])

		return Response(SellerApplicationSerializer(application).data, status=status.HTTP_200_OK)
