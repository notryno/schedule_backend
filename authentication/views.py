# views.py

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        data = {
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
        }
        return Response(data, status=status.HTTP_201_CREATED)

class LoginView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user, created = CustomUser.objects.get_or_create(email=serializer.validated_data['email'])

        refresh = RefreshToken.for_user(user)
        data = {
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
        }
        return Response(data, status=status.HTTP_200_OK)
