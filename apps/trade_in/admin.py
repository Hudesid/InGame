from django.contrib import admin
from .models import TradeIn


@admin.register(TradeIn)
class TradeInAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'telegram_nik', 'status', 'config')
    list_filter = ('created_at', 'updated_at', 'status')
    search_fields = ('id', 'name', 'phone', 'telegram_nik')
    readonly_fields = ('id', 'created_at', 'updated_at')