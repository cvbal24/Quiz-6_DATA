from django.urls import path

from .views import (
    ListServicesView,
    SellerCreateServiceView,
    SellerManageServiceView,
    ServiceDetailView,
)

urlpatterns = [
    path('list/', ListServicesView.as_view(), name='services-list'),
    path('<int:pk>/', ServiceDetailView.as_view(), name='services-detail'),
    path('manage/', SellerCreateServiceView.as_view(), name='services-create'),
    path('manage/<int:pk>/', SellerManageServiceView.as_view(), name='services-manage'),
]
