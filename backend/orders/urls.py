from django.urls import path

from .views import CreateOrderView, OrderHistoryView

urlpatterns = [
    path('create/', CreateOrderView.as_view(), name='orders-create'),
    path('history/', OrderHistoryView.as_view(), name='orders-history'),
]
