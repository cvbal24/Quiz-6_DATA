from django.contrib import admin
from .models import SubscriptionTier, UserSubscription


class SubscriptionTierAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'max_usage', 'created_at')
    search_fields = ('name',)
    list_filter = ('price', 'created_at')


class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'tier', 'usage_left', 'is_active', 'subscribed_at')
    search_fields = ('user__email', 'tier__name')
    list_filter = ('is_active', 'tier', 'subscribed_at')
    readonly_fields = ('subscribed_at', 'updated_at')


admin.site.register(SubscriptionTier, SubscriptionTierAdmin)
admin.site.register(UserSubscription, UserSubscriptionAdmin)
