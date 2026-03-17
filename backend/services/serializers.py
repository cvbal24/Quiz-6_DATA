from rest_framework import serializers

from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    seller_first_name = serializers.CharField(source='seller.first_name', read_only=True)
    seller_last_name = serializers.CharField(source='seller.last_name', read_only=True)
    seller_email = serializers.CharField(source='seller.email', read_only=True)

    class Meta:
        model = Service
        fields = [
            'id',
            'seller',
            'seller_first_name',
            'seller_last_name',
            'seller_email',
            'service_name',
            'description',
            'price',
            'duration_of_service',
            'sample_image',
            'rating',
            'expert',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'seller', 'created_at', 'updated_at']


class ServiceManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'id',
            'service_name',
            'description',
            'price',
            'duration_of_service',
            'sample_image',
            'rating',
            'expert',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
