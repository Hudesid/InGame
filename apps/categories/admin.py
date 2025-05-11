from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_uz', 'name_ru', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('id', 'name_uz', 'name_ru', 'description_uz', 'description_uz')
    readonly_fields = ('id', 'created_at', 'updated_at')
