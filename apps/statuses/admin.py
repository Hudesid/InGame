from django.contrib import admin
from .models import Status


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'updated_at', 'created_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('id', 'name')
    readonly_fields = ('id', 'created_at', 'updated_at')