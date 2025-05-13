from django.contrib import admin
from .models import Order, OrderDesktopItem, OrderProductItem


class OrderDesktopItemInLine(admin.TabularInline):
    model = OrderDesktopItem
    extra = 1
    raw_id_fields = ('order',)


class OrderProductItemInLine(admin.TabularInline):
    model = OrderProductItem
    extra = 1
    raw_id_fields = ('order',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'customer_phone', 'address', 'total_price', 'status')
    list_filter = ('created_at', 'updated_at', 'total_price', 'status', 'delivery_method')
    search_fields = ('id', 'customer_name', 'customer_phone', 'address', 'comment')
    readonly_fields = ('id', 'created_at', 'updated_at')
    inlines = [OrderDesktopItemInLine, OrderProductItemInLine]


@admin.register(OrderDesktopItem)
class OrderDesktopItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'quantity', 'credit_term', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'desktop', 'order', 'quantity', 'credit', 'edit_product')
    search_fields = ('id',)
    readonly_fields = ('id', 'created_at', 'updated_at')


@admin.register(OrderProductItem)
class OrderProductItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'quantity', 'credit_term', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'product', 'order', 'quantity', 'credit')
    search_fields = ('id',)
    readonly_fields = ('id', 'created_at', 'updated_at')