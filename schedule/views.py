from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Schedule, SpecialSchedule
from .serializers import ScheduleSerializer, SpecialScheduleSerializer


class ScheduleListView(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(user=request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# class ScheduleListView(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]

#     def list(self, request, *args, **kwargs):
#         schedules = Schedule.objects.filter(user=request.user)
#         schedule_serializer = ScheduleSerializer(schedules, many=True)

#         special_schedules = SpecialSchedule.objects.filter(schedule__user=request.user)
#         special_schedule_serializer = SpecialScheduleSerializer(
#             special_schedules, many=True
#         )

#         data = {
#             "schedules": schedule_serializer.data,
#             "special_schedules": special_schedule_serializer.data,
#         }

#         return Response(data, status=status.HTTP_200_OK)


class SpecialScheduleListView(generics.ListCreateAPIView):
    serializer_class = SpecialScheduleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SpecialSchedule.objects.select_related("schedule").filter(
            schedule__user=self.request.user
        )

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
