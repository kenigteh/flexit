from rest_framework import serializers

from rest.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['login', 'status', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def check_user(self, validated_data):
        try:
            User.objects.get(login=validated_data.get('login'))
            return False
        except:
            return True

    def create(self, validated_data):
        if self.check_user(validated_data):
            user = User.objects.create(**validated_data)
            return user
        else:
            return False

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.username)
        instance.password = validated_data.get('password', instance.email)
        instance.save()
        return instance
