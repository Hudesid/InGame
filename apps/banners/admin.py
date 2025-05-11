from django.contrib import admin
from .models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_uz', 'name_ru')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('id', 'name_uz', 'name_ru', 'description_uz', 'description_ru', 'url')
    readonly_fields = ('id', 'created_at', 'updated_at')