from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .models import SkillType
from .serializers import SkillTypeSerializer

User = get_user_model()


class SkillTypeViewSet(viewsets.ModelViewSet):

    queryset = SkillType.objects.all()
    serializer_class = SkillTypeSerializer
