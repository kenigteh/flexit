from rest_framework import serializers

from rest.models import Bonus


class BonusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bonus
        fields = ['bonus_code', 'user_id', 'active_time']

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.active_time = validated_data.get('active_time', instance.active_time)
        instance.status = 3
        instance.save()
        return instance
