from django.contrib import admin
from .models import New


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    exclude = ('title', 'description')
    list_display = ('id', 'display_title_uz', 'display_title_ru', 'created_at')
    list_filter = ('created_at', 'updated_at', 'youtube_url')
    search_fields = ('id', 'title_uz', 'title_ru', 'description_uz', 'description_ru', 'youtube_url')
    readonly_fields = ('id', 'created_at', 'updated_at')


    def display_title_uz(self, obj):
        return obj.title_uz
    display_title_uz.short_description = 'Title (UZ)'

    def display_title_ru(self, obj):
        return obj.title_ru
    display_title_ru.short_description = 'Title (RU)'