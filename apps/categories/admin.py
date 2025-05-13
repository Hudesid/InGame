from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('name', 'description')
    list_display = ('id', 'display_name_uz', 'display_name_ru', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('id', 'name_uz', 'name_ru', 'description_uz', 'description_uz')
    readonly_fields = ('id', 'created_at', 'updated_at')


    def display_name_uz(self, obj):
        return obj.name_uz
    display_name_uz.short_description = 'Name (UZ)'

    def display_name_ru(self, obj):
        return obj.name_ru
    display_name_ru.short_description = 'Name (RU)'