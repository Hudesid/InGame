from rest_framework import serializers
from .models import Game, Fps


class FpsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fps
        fields = ('id', 'game_fps', 'desktop')


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'game_name', 'game_image', 'fps')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['fps'] = FpsSerializer(instance.fps, many=True).data
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class GameFpsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fps
        fields = ('id', 'game_fps', 'game')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['game'] = GameSerializer(instance.game).data
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation