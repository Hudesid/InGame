from django.contrib import admin
from .models import Service, ServiceName


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'type', 'price', 'status')
    list_filter = ('created_at', 'updated_at', 'type', 'price', 'status')
    search_fields = ('id', 'name', 'phone', 'other_services')
    readonly_fields = ('id', 'created_at', 'updated_at')


@admin.register(ServiceName)
class ServiceNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'service')
    search_fields = ('id', 'name')
    readonly_fields = ('id', 'created_at', 'updated_at')