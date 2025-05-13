from django.contrib import admin
from .models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    exclude = ('name', 'description')
    list_display = ('id', 'display_name_uz', 'display_name_ru')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('id', 'name_uz', 'name_ru', 'description_uz', 'description_ru', 'url')
    readonly_fields = ('id', 'created_at', 'updated_at')


    def display_name_uz(self, obj):
        return obj.name_uz
    display_name_uz.short_description = 'Name (UZ)'

    def display_name_ru(self, obj):
        return obj.name_ru
    display_name_ru.short_description = 'Name (RU)'