from rest_framework import serializers
from .models import Catalog


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ('id', 'name_uz', 'name_ru', 'image', 'type')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation