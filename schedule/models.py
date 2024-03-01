from datetime import timedelta

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()
    type = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    description = models.TextField()
    number_of_instances = models.IntegerField(default=1)
    frequency_per_week = models.IntegerField(
        default=1
    )  # For example, 1 for daily, 7 for weekly
    day_of_week = models.IntegerField(
        choices=[(i, i) for i in range(1, 8)], default=1
    )  # 1 for Monday, 2 for Tuesday, ..., 7 for Sunday

    def generate_schedule(self):
        schedule = []
        current_date = timezone.now().date()
        for i in range(self.number_of_instances):
            current_date = current_date + timedelta(days=self.frequency_per_week)
            weekday = (
                current_date.weekday()
            )  # 0 for Monday, 1 for Tuesday, ..., 6 for Sunday
            if weekday == self.day_of_week:
                schedule.append(
                    {
                        "date": current_date,
                        "title": self.title,
                        "start_time": self.start_time,
                        "end_time": self.end_time,
                        "type": self.type,
                        "location": self.location,
                        "description": self.description,
                    }
                )
        return schedule
