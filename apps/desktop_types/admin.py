from django.contrib import admin
from .models import DesktopType


@admin.register(DesktopType)
class DesktopTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('id', 'name')
    readonly_fields = ('id', 'created_at', 'updated_at')
