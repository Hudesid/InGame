from rest_framework import serializers
from apps.categories.serializers import CategorySerializer
from .models import Attribute



class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('id', 'type_uz', 'type_ru', 'value', 'category')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        representation['category'] = CategorySerializer(instance.category).data
        return representation


class SearchSerializer(serializers.Serializer):
    q = serializers.CharField(max_length=255, required=True)

    def validate_q(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Search query cannot be empty")
        return value