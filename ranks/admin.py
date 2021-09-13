from django.contrib import admin

from .models import VotedRank, WallRank

admin.site.register(WallRank)
admin.site.register(VotedRank)
