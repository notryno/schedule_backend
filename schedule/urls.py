from django.urls import path

from . import views
from .views import ScheduleListView

urlpatterns = [
    path("schedule/", views.ScheduleListView.as_view(), name="schedule-list"),
    # path(
    #     "schedule/<int:pk>/", views.ScheduleDetailView.as_view(), name="schedule-detail"
    # ),
    path("schedules/", ScheduleListView.as_view(), name="schedule-list"),
]
