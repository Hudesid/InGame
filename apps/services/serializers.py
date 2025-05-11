from rest_framework import serializers
from .models import Service, ServiceName


class ServiceNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceName
        fields = ('id', 'name')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class ServiceSerializer(serializers.ModelSerializer):
    services = serializers.ListField(child=serializers.CharField(max_length=255), required=True, write_only=True)

    class Meta:
        model = Service
        fields = ('id', 'name', 'phone', 'type', 'price', 'other_services', 'services')


    def create(self, validated_data):
        services = validated_data.pop('services', [])
        service = Service.objects.create(**validated_data)
        for name in services:
            ServiceName.objects.create(name=name, service=service)
        return service


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        representation['services'] = ServiceNameSerializer(instance.services, many=True).data
        return representation


