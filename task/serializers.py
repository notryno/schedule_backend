from rest_framework import serializers

from authentication.serializers import UserSerializer

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "user",
            "title",
            "description",
            "completed",
            "created_at",
            "due_date",
            "due_time",
            "all_day",
        ]
