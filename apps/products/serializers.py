from rest_framework import serializers
from .models import Product, ProductImage



class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'image')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name_uz', 'name_ru', 'description_uz', 'description_ru', 'price', 'category', 'brand', 'discount', 'attributes', 'statuses', 'type', 'images')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        from apps.brands.serializers import BrandSerializer
        from apps.categories.serializers import CategorySerializer
        from apps.attributes.serializers import AttributeSerializer
        from apps.statuses.serializers import StatusSerializer
        from apps.product_types.serializers import ProductTypeSerializer
        representation['category'] = CategorySerializer(instance.category).data
        representation['brand'] = BrandSerializer(instance.brand).data
        representation['attributes'] = AttributeSerializer(instance.attributes, many=True).data
        representation['statuses'] = StatusSerializer(instance.statuses, many=True).data
        representation['type'] = ProductTypeSerializer(instance.type).data
        representation['images'] = ProductImageSerializer(instance.images, many=True).data
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation

