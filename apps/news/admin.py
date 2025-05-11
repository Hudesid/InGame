from django.contrib import admin
from .models import New


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_uz', 'title_ru', 'created_at')
    list_filter = ('created_at', 'updated_at', 'youtube_url')
    search_fields = ('id', 'title_uz', 'title_ru', 'description_uz', 'description_ru', 'youtube_url')
    readonly_fields = ('id', 'created_at', 'updated_at')
