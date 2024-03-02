from rest_framework import serializers

from .models import Schedule, SpecialSchedule


class ScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        fields = "__all__"  # Include all fields in the serializer


class SpecialScheduleSerializer(serializers.ModelSerializer):
    schedule = ScheduleSerializer()

    class Meta:
        model = SpecialSchedule
        fields = "__all__"  # You can include specific fields if needed
