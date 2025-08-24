# accounts/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "bio", "profile_picture", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            email=validated_data.get("email", ""),
            bio=validated_data.get("bio", ""),
            profile_picture=validated_data.get("profile_picture", ""),
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
