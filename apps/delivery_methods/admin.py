from django.contrib import admin
from .models import DeliveryMethod


@admin.register(DeliveryMethod)
class DeliveryMethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_uz', 'name_ru', 'price', 'estimated_delivery_time')
    list_filter = ('created_at', 'updated_at', 'price', 'estimated_delivery_time')
    search_fields = ('id', 'name_uz', 'name_ru')
    readonly_fields = ('id', 'created_at', 'updated_at')
