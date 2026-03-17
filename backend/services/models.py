from django.db import models


class Service(models.Model):
    seller = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='services')
    service_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_of_service = models.CharField(max_length=255)
    sample_image = models.ImageField(upload_to='services/')
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    expert = models.CharField(max_length=255, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.service_name} by {self.seller.email}'

    class Meta:
        ordering = ['-created_at']
