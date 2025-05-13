from django.contrib import admin
from .models import Attribute


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    exclude = ('type',)
    list_display = ('id', 'display_type_uz', 'display_type_ru', 'value', 'created_at')
    list_filter = ('value', 'created_at', 'updated_at', 'category')
    search_fields = ('type_uz', 'type_ru')
    readonly_fields = ('id', 'created_at', 'updated_at')


    def display_type_uz(self, obj):
        return obj.type_uz
    display_type_uz.short_description = 'Type (UZ)'

    def display_type_ru(self, obj):
        return obj.type_ru
    display_type_ru.short_description = 'Type (RU)'