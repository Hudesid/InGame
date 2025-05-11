from rest_framework import serializers
from .models import Comment, ProductComment, DesktopComment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('username', 'comment_uz', 'comment_ru', 'description_uz', 'description_ru', 'image', 'video')


    def validate_video(self, value):
        max_size = 500 * 1024 * 1024
        if value and value.size > max_size:
            raise serializers.ValidationError("Video 500 MB dan katta bo'lishi mumkin emas.")
        return value


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class ProductCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductComment
        fields = ('id', 'product', 'username', 'comment', 'image', 'rating')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class DesktopCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesktopComment
        fields = ('id', 'desktop', 'username', 'comment', 'image', 'rating')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation