from django.contrib import admin
from .models import DeliveryMethod


@admin.register(DeliveryMethod)
class DeliveryMethodAdmin(admin.ModelAdmin):
    exclude = ('name',)
    list_display = ('id', 'display_name_uz', 'display_name_ru', 'price', 'estimated_delivery_time')
    list_filter = ('created_at', 'updated_at', 'price', 'estimated_delivery_time')
    search_fields = ('id', 'name_uz', 'name_ru')
    readonly_fields = ('id', 'created_at', 'updated_at')


    def display_name_uz(self, obj):
        return obj.name_uz
    display_name_uz.short_description = 'Name (UZ)'

    def display_name_ru(self, obj):
        return obj.name_ru
    display_name_ru.short_description = 'Name (RU)'