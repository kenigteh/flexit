from rest_framework import serializers

from rest.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['login', 'password', 'status']

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.username)
        instance.password = validated_data.get('password', instance.email)
        instance.save()
        return instance
