from django.contrib import admin

from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'service_name', 'seller', 'price', 'created_at')
    list_filter = ('seller', 'created_at')
    search_fields = ('service_name', 'description', 'seller__email')
    readonly_fields = ('created_at', 'updated_at')
