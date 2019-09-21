from rest_framework import serializers

from rest.models import Bonus


class BonusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bonus
        fields = ['bonus_code', 'fas_time', 'type']

    def create(self, validated_data):
        user = Bonus.objects.create(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.status = 1
        instance.fas_time = validated_data.get('fas_time', instance.username)
        instance.type = validated_data.get('type', instance.email)
        instance.save()
        return instance
