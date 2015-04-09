from Salus import models
from rest_framework import serializers


class SimplePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Password
        fields = ('id', 'title', 'password')


class FullPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Password
        fields = ('id', 'title', 'password', 'url', 'notes', 'created_at', 'updated_at')