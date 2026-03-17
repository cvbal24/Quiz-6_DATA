from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import CustomUser
from .permissions import IsAdminRole
from .serializers import (
	AdminUserManagementSerializer,
	MyTokenObtainPairSerializer,
	RegisterSerializer,
	UserSerializer,
)


class LoginView(TokenObtainPairView):
	serializer_class = MyTokenObtainPairSerializer
	permission_classes = [permissions.AllowAny]


class RegisterView(generics.CreateAPIView):
	queryset = CustomUser.objects.all()
	serializer_class = RegisterSerializer
	permission_classes = [permissions.AllowAny]


class ProfileView(APIView):
	permission_classes = [permissions.IsAuthenticated]

	def get(self, request):
		serializer = UserSerializer(request.user)
		return Response(serializer.data)


class AdminUserListView(generics.ListAPIView):
	queryset = CustomUser.objects.all().order_by('-id')
	serializer_class = AdminUserManagementSerializer
	permission_classes = [IsAdminRole]


class AdminUserDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = CustomUser.objects.all()
	serializer_class = AdminUserManagementSerializer
	permission_classes = [IsAdminRole]
