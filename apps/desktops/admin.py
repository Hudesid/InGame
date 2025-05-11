from django.contrib import admin
from .models import Desktop, DesktopImage
from apps.desktops_fps.models import Fps


class FpsInLine(admin.TabularInline):
    model = Fps
    extra = 1
    raw_id_fields = ('desktop',)


class DesktopImageInLine(admin.TabularInline):
    model = DesktopImage
    extra = 1
    raw_id_fields = ('desktop',)


@admin.register(Desktop)
class DesktopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_uz', 'name_ru', 'price', 'type', 'created_at')
    list_filter = ('created_at', 'updated_at', 'category', 'desktop_types', 'attributes', 'price', 'products', 'statuses', 'type')
    search_fields = ('id', 'name_uz', 'name_ru', 'description_uz', 'description_ru')
    readonly_fields = ('id', 'created_at', 'updated_at')
    inlines = [DesktopImageInLine, FpsInLine]
    prepopulated_fields = {
        "slug": ('name_uz',)
    }


@admin.register(DesktopImage)
class DesktopImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'desktop')
    search_fields = ('id',)
    readonly_fields = ('id', 'created_at', 'updated_at')