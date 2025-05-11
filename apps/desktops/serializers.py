from rest_framework import serializers
from .models import Desktop, DesktopImage


class DesktopImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesktopImage
        fields = ('id', 'image')


class DesktopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desktop
        fields = ('id', 'name_uz', 'name_ru', 'type', 'desktop_types', 'description_uz', 'description_ru', 'price', 'statuses', 'products', 'category', 'images', 'fps', 'attributes')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        from apps.desktop_types.serializers import DesktopTypeSerializer
        from apps.statuses.serializers import StatusSerializer
        from apps.products.serializers import ProductSerializer
        from apps.categories.serializers import CategorySerializer
        from apps.desktops_fps.serializers import GameFpsSerializer
        from apps.attributes.serializers import AttributeSerializer
        representation['attributes'] = AttributeSerializer(instance.attributes, many=True).data
        representation['fps'] = GameFpsSerializer(instance.fps, many=True).data
        representation['desktop_types'] = DesktopTypeSerializer(instance.desktop_types, many=True).data
        representation['statuses'] = StatusSerializer(instance.statuses, many=True).data
        representation['products'] = ProductSerializer(instance.products, many=True).data
        representation['images'] = DesktopImageSerializer(instance.images, many=True).data
        representation['category'] = CategorySerializer(instance.category).data
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation
