from django.contrib import admin

from .models import Skill, SkillType

admin.site.register(SkillType)
admin.site.register(Skill)
