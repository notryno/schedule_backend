# authentication/serializers.py

from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    profile_picture = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = CustomUser
        fields = ['email','password', 'first_name', 'last_name', 'profile_picture']

    def to_representation(self, instance):
        if isinstance(instance, CustomUser):
            representation = super().to_representation(instance)
            representation['profile_picture'] = instance.profile_picture.url if instance.profile_picture else None
            return representation
        return instance

    def create(self, validated_data):
        profile_picture = validated_data.pop('profile_picture', None)
        user = super().create(validated_data)
        if profile_picture:
            user.profile_picture = profile_picture
            user.save()
        return user