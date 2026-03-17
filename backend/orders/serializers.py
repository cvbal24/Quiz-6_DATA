from rest_framework import serializers

from services.models import Service

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    buyer_email = serializers.CharField(source='buyer.email', read_only=True)
    buyer_first_name = serializers.CharField(source='buyer.first_name', read_only=True)
    buyer_last_name = serializers.CharField(source='buyer.last_name', read_only=True)
    service_name = serializers.CharField(source='service.service_name', read_only=True)
    service_seller_email = serializers.CharField(source='service.seller.email', read_only=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'buyer',
            'buyer_email',
            'buyer_first_name',
            'buyer_last_name',
            'service',
            'service_name',
            'service_seller_email',
            'paypal_transaction_id',
            'price_paid',
            'date_purchased',
        ]
        read_only_fields = ['id', 'buyer', 'date_purchased']


class OrderCreateSerializer(serializers.Serializer):
    service = serializers.IntegerField()
    paypal_transaction_id = serializers.CharField(max_length=255)
    price_paid = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate_service(self, value):
        try:
            return Service.objects.get(pk=value)
        except Service.DoesNotExist:
            raise serializers.ValidationError('Service not found.')

    def create(self, validated_data):
        service = validated_data.pop('service')
        order = Order.objects.create(service=service, **validated_data)
        return order
