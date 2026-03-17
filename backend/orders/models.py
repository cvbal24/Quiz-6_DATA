from django.db import models


class Order(models.Model):
    buyer = models.ForeignKey('users.CustomUser', on_delete=models.SET_NULL, null=True, related_name='orders_as_buyer')
    service = models.ForeignKey('services.Service', on_delete=models.SET_NULL, null=True, related_name='orders')
    paypal_transaction_id = models.CharField(max_length=255, unique=True)
    price_paid = models.DecimalField(max_digits=10, decimal_places=2)
    date_purchased = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.id} - {self.buyer.email} for {self.service.service_name}'

    class Meta:
        ordering = ['-date_purchased']
