from django.contrib import admin
from .models import LeaveRequest


@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'status', 'created_at')
    list_filter = ('created_at', 'updated_at', 'status')
    search_fields = ('id', 'name', 'phone', 'operator_commit')
    readonly_fields = ('id', 'created_at', 'updated_at')
