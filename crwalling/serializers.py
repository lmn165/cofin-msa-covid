from rest_framework import serializers
from .models import Today as today, Week_avg as week

class TodaySerializer(serializers.Serializer):
    death = serializers.CharField()
    serious = serializers.CharField()
    new_hospitalization = serializers.CharField()
    confirmed = serializers.CharField()
    update_at = serializers.DateTimeField()

    class Meta:
        model = today
        fields = '__all__'

    def create(self, validated_data):
        return today.objects.create(**validated_data)

    def update(self, instance, validated_data):
        today.objects.filter(pk=instance.id).update(**validated_data)

class WeekSerializer(serializers.Serializer):
    death = serializers.CharField()
    serious = serializers.CharField()
    new_hospitalization = serializers.CharField()
    confirmed = serializers.CharField()
    update_at = serializers.DateTimeField()

    class Meta:
        model = week
        fields = '__all__'

    def create(self, validated_data):
        return week.objects.create(**validated_data)

    def update(self, instance, validated_data):
        week.objects.filter(pk=instance.id).update(**validated_data)
