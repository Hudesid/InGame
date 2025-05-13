from django.contrib import admin
from .models import Product, ProductImage


class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    extra = 1
    raw_id_fields = ('product',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ('name', 'description')
    list_display = ('id', 'display_name_uz', 'display_name_ru', 'price', 'discount')
    list_filter = ('created_at', 'updated_at', 'discount', 'price', 'category', 'brand', 'attributes', 'statuses', 'type')
    search_fields = ('id', 'name_uz', 'name_ru', 'description_uz', 'description_ru')
    readonly_fields = ('id', 'created_at', 'updated_at')
    prepopulated_fields = {"slug": ('name_uz',)}
    inlines = [ProductImageInLine]


    def display_name_uz(self, obj):
        return obj.name_uz
    display_name_uz.short_description = 'Name (UZ)'

    def display_name_ru(self, obj):
        return obj.name_ru
    display_name_ru.short_description = 'Name (RU)'


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'product')
    search_fields = ('id',)
    readonly_fields = ('id', 'created_at', 'updated_at')