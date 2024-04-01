from rest_framework import generics, status
from .models import Classroom
from .serializers import ClassroomSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class ClassroomViewList(generics.ListCreateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
