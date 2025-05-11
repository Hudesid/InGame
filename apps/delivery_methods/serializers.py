from rest_framework import serializers
from .models import DeliveryMethod


class DeliveryMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryMethod
        fields = ('id', 'name_uz', 'name_ru', 'price', 'estimated_delivery_time', 'logo')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation