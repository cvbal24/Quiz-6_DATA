from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'buyer', 'service', 'price_paid', 'date_purchased')
    list_filter = ('date_purchased', 'buyer')
    search_fields = ('buyer__email', 'service__service_name', 'paypal_transaction_id')
    readonly_fields = ('date_purchased',)
