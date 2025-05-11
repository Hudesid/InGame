from django.contrib import admin
from .models import Credit


@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'bank_credit', 'months', 'created_at')
    list_filter = ('created_at', 'updated_at', 'months', 'bank_credit')
    search_fields = ('id', 'name')
    readonly_fields = ('id', 'created_at', 'updated_at')
