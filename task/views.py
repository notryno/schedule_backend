from django.http import JsonResponse
from models import Task
from rest_framework import generics, permissions

from .serializers import TaskSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    print("TaskListCreateView")
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        try:
            # Associate the task with the authenticated user
            serializer.save(user=self.request.user)
        except Exception as e:
            # Log the exception for debugging
            print(f"Error creating task: {e}")
            return JsonResponse({"error": str(e)}, status=400)


class TaskRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    print("TaskRetrieveUpdateDeleteView")
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
