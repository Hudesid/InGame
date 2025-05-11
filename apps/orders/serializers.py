from rest_framework import serializers
from .models import Order, OrderDesktopItem, OrderProductItem
from apps.desktops.serializers import Desktop
from apps.credits.serializers import CreditSerializer, Credit
from apps.products.serializers import Product
from apps.delivery_methods.serializers import DeliveryMethodSerializer


class DesktopShortSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='desktop', lookup_field='slug')

    class Meta:
        model = Desktop
        fields = ('id', 'name_uz', 'name_ru', 'price', 'url')


class ProductShortSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='product', lookup_field='slug')

    class Meta:
        model = Desktop
        fields = ('id', 'name_uz', 'name_ru', 'price', 'url')


class OrderDesktopItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDesktopItem
        fields = ('id', 'desktop', 'quantity', 'credit', 'credit_term', 'edit_product')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        representation['desktop'] = DesktopShortSerializer(instance.desktop, context={'request': request}).data
        representation['credit'] = CreditSerializer(instance.credit).data
        representation['edit_product'] = ProductShortSerializer(instance.edit_product, many=True, context={'request': request}).data
        return representation


class OrderProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProductItem
        fields = ('id', 'product', 'quantity', 'credit', 'credit_term')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        representation['credit'] = CreditSerializer(instance.credit).data
        representation['product'] = ProductShortSerializer(instance.product, context={'request': request}).data
        return representation


class OrderSerializer(serializers.ModelSerializer):
    products = serializers.ListField(child=serializers.DictField(), write_only=True, required=True)

    class Meta:
        model = Order
        fields = ('id', 'customer_name', 'customer_phone', 'address', 'comment', 'delivery_method', 'total_price', 'products')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        representation['delivery_method'] = DeliveryMethodSerializer(instance.delivery_method).data
        products = []
        products += OrderProductItemSerializer(instance.product_items, many=True).data
        products += OrderDesktopItemSerializer(instance.desktop_items, many=True).data
        representation['products'] = products
        return representation


    def create(self, validated_data):
        products = validated_data.pop('products', [])
        order = Order.objects.create(**validated_data)
        for product in products:
            if 'desktop' in product:
                edit_product = product.pop('edit_product', [])
                desktop = Desktop.objects.get(id=product.pop('desktop'))
                credit = Credit.objects.get(id=product.pop('credit'))
                item = OrderDesktopItem.objects.create(desktop=desktop, order=order, credit=credit, **product)
                item.edit_product.set(edit_product)
            else:
                credit = Credit.objects.get(id=product.pop('credit'))
                product_id = Product.objects.get(id=product.pop('product'))
                OrderProductItem.objects.create(product=product_id, order=order, credit=credit, **product)

        return order


