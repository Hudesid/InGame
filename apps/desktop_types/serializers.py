from rest_framework import serializers
from .models import DesktopType


class DesktopTypeSerializer(serializers.Serializer):
    class Meta:
        model = DesktopType
        fields = ('id', 'name')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation