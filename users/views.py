from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import CreateAPIView
from .models import FamilyGroup
from .serializers import UserProfileSerializer, UserRegistrationSerializer


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        mode = request.data.get('profile_mode')

        if mode not in ['personal', 'family']:
            return Response({'error': 'Invalid profile mode'}, status=status.HTTP_400_BAD_REQUEST)

        user.profile_mode = mode

        if mode == 'family':
            family_group, created = FamilyGroup.objects.get_or_create(name=f"{user.username}'s family")
            user.family_group = family_group
        else:
            user.family_group = None

        user.save()
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)


class RegisterUserView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
