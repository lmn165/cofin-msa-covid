from rest_framework import serializers
from .models import drive

class ConfirmedSerializers(serializers.Serializer):
    date = serializers.DateTimeField()
    confirmed = serializers.CharField()

    class Meta:
        model = drive
        fields = '__all__'

    def create(self, validated_data):
        return drive.objects.create(**validated_data)

    def update(self, instance, validated_data):
        drive.objects.filter(pk=instance.id).update(**validated_data)
