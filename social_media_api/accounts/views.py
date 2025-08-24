from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer, LoginResponseSerializer
from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import UserRegistrationSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from .models import CustomUser
from rest_framework.views import APIView
from .models import CustomUser

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email,
            "bio": user.bio,
            "profile_picture": user.profile_picture.url if user.profile_picture else None,
            "followers_count": user.followers.count(),
        })
    



User = get_user_model()


class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        for user in CustomUser.objects.all():  
            if user.id == user_id:
                request.user.following.add(user)
                return Response({"detail": f"You are now following {user.username}"})
        return Response({"error": "User not found"}, status=404)


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        for user in CustomUser.objects.all():  
            if user.id == user_id:
                request.user.following.remove(user)
                return Response({"detail": f"You unfollowed {user.username}"})
        return Response({"error": "User not found"}, status=404)

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        request.user.following.add(user_to_follow)  
        return Response({"detail": f"You are now following {user_to_follow.username}"})


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({"detail": f"You unfollowed {user_to_unfollow.username}"})
