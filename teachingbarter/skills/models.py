from django.db import models
from django_extensions.db.models import TimeStampedModel


class SkillType(TimeStampedModel):
    type = models.CharField(max_length=24)

    def __str__(self):
        return self.type


class Skill(TimeStampedModel):
    skill_type = models.ForeignKey(SkillType, on_delete=models.CASCADE)
    skill = models.CharField(max_length=24)

    def __str__(self):
        return self.skill
