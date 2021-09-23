from django.db import models
from django_extensions.db.models import TimeStampedModel


class SkillType(TimeStampedModel):
    type = models.CharField(max_length=24, unique=True)

    class Meta:
        ordering = ["type"]

    def __str__(self):
        return self.type


class Skill(TimeStampedModel):
    skill_type = models.ForeignKey(SkillType, on_delete=models.CASCADE)
    skill = models.CharField(max_length=24, unique=True)

    @property
    def get_teachers(self):
        teachers = self.userwall_set.all()
        return teachers

    class Meta:
        ordering = ["skill"]

    def __str__(self):
        return self.skill
