from rest_framework import serializers

from wall.models import UserWall

from .models import Skill, SkillType


class SkillTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillType
        fields = ["id", "type"]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["id", "skill_type", "skill"]


class SkillTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWall
        fields = ["id", "user", "get_username", "get_rank", "avatar"]
