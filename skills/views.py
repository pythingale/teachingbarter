from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .models import Skill, SkillType
from .serializers import SkillSerializer, SkillTeacherSerializer, SkillTypeSerializer

# from rest_framework.filters import OrderingFilter


User = get_user_model()


class SkillTypeViewSet(viewsets.ModelViewSet):

    queryset = SkillType.objects.all()
    serializer_class = SkillTypeSerializer

    def retrieve(self, request, pk=None):
        queryset = Skill.objects.filter(skill_type=pk)
        serializer = SkillSerializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        raise PermissionDenied

    def get_permissions(self):
        if self.action == "list" or "retrieve":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class SkillViewSet(viewsets.ModelViewSet):

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def retrieve(self, request, pk=None):
        queryset = Skill.objects.get(id=pk).get_teachers
        serializer = SkillTeacherSerializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        raise PermissionDenied

    def get_permissions(self):
        if self.action == "list" or "retrieve":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
