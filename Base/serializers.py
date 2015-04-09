from Base import models
from rest_framework import serializers


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RangoUser
        fields = ('id', 'username', 'email', 'avatar')


class FullUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RangoUser
        fields = ('id', 'username', 'nickname', 'fullname', 'email', 'birthday', 'avatar')