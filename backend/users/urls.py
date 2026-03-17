from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import AdminUserDetailView, AdminUserListView, LoginView, ProfileView, RegisterView

urlpatterns = [
    path('login/', LoginView.as_view(), name='users-login'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', ProfileView.as_view(), name='users-profile'),
    path('admin/users/', AdminUserListView.as_view(), name='users-admin-list'),
    path('admin/users/<int:pk>/', AdminUserDetailView.as_view(), name='users-admin-detail'),
    path('token/refresh/', TokenRefreshView.as_view(), name='users-token-refresh'),
]
