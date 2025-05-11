from rest_framework import serializers
from .models import New


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ('id', 'title_uz', 'title_ru', 'description_uz', 'description_ru', 'youtube_url')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation