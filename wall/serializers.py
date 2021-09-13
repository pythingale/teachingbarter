from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import UserWall

User = get_user_model()


class UserWallSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWall
        fields = ("user", "description", "skills", "rank", "vote_numbers", "avatar")
        read_only_fields = ("user", "vote_numbers")
