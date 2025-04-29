from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import FamilyGroup
from dj_rest_auth.registration.serializers import RegisterSerializer

User = get_user_model()


class CustomRegisterSerializer(RegisterSerializer):
    profile_mode = serializers.ChoiceField(choices=User.MODE_CHOICES, default='personal')

    def custom_signup(self, request, user):
        user.profile_mode = self.validated_data.get('profile_mode', 'personal')
        user.save()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'profile_mode']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            profile_mode=validated_data.get('profile_mode', 'personal')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class FamilyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyGroup
        fields = ['id', 'name', 'created_at']


class UserProfileSerializer(serializers.ModelSerializer):
    family_group = FamilyGroupSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile_mode', 'family_group']