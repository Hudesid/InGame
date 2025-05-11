from rest_framework import serializers
from .models import TradeIn


class TradeInSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeIn
        fields = ('id', 'name', 'phone', 'telegram_nik', 'config')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation