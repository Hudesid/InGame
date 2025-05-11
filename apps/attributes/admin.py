from django.contrib import admin
from .models import Attribute


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_uz', 'type_ru', 'value', 'created_at')
    list_filter = ('value', 'created_at', 'updated_at', 'category')
    search_fields = ('type_uz', 'type_ru')
    readonly_fields = ('id', 'created_at', 'updated_at')