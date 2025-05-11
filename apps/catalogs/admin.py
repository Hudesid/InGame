from django.contrib import admin
from .models import Catalog


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_uz', 'name_ru', 'type', 'created_at')
    list_filter = ('created_at', 'updated_at', 'type')
    search_fields = ('id', 'name_uz', 'name_ru')
    readonly_fields = ('id', 'created_at', 'updated_at')