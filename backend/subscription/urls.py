from django.urls import path
from .views import ListTiersView, SubscribeView, CurrentSubscriptionView, AdminSubscriptionListView

urlpatterns = [
    path('tiers/', ListTiersView.as_view(), name='list_tiers'),
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('current/', CurrentSubscriptionView.as_view(), name='current_subscription'),
    path('list/', AdminSubscriptionListView.as_view(), name='admin_subscription_list'),
]
