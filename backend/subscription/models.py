from django.db import models
from users.models import CustomUser


class SubscriptionTier(models.Model):
    """Subscription tier with pricing and usage limits."""
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    max_usage = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['price']

    def __str__(self):
        return f"{self.name} - ${self.price} ({self.max_usage} uses)"


class UserSubscription(models.Model):
    """Track user subscriptions and usage."""
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='subscription')
    tier = models.ForeignKey(SubscriptionTier, on_delete=models.SET_NULL, null=True, related_name='subscribers')
    usage_left = models.IntegerField()
    is_active = models.BooleanField(default=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-subscribed_at']

    def __str__(self):
        return f"{self.user.email} - {self.tier.name if self.tier else 'No Tier'} ({self.usage_left} left)"
