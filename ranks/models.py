from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_extensions.db.models import TimeStampedModel

from wall.models import UserWall

User = get_user_model()


class WallRank(TimeStampedModel):
    wall = models.OneToOneField(
        UserWall, on_delete=models.CASCADE, related_name="wall_rank"
    )
    rank = models.FloatField(blank=True, null=True)
    voters = models.PositiveIntegerField(default=0)

    @receiver(post_save, sender=UserWall)
    def create_wall_Rank(sender, instance, created, **kwargs):
        if created:
            WallRank.objects.create(wall=instance)

    def __str__(self):
        return self.wall.user.username


class VotedRank(TimeStampedModel):
    wall_rank = models.ForeignKey(
        WallRank, on_delete=models.CASCADE, related_name="voted_rank"
    )
    voter = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="rank_voter",
    )

    INCREDIBLE = 10
    BRILLIANT = 9
    FANTASTIC = 8
    VERYGOOD = 7
    GOOD = 6
    AVERAGE = 5
    BELOWAVERAGE = 4
    BAD = 3
    VERYBAD = 2
    AWFUL = 1

    CHOICES = (
        (INCREDIBLE, "incredible"),
        (BRILLIANT, "brilliant"),
        (FANTASTIC, "fantastic"),
        (VERYGOOD, "very good"),
        (GOOD, "good"),
        (AVERAGE, "average"),
        (BELOWAVERAGE, "below average"),
        (BAD, "bad"),
        (VERYBAD, "very_bad"),
        (AWFUL, "awful"),
    )
    rank = models.PositiveSmallIntegerField(choices=CHOICES)

    def __str__(self):
        return str(self.rank)


@receiver(post_save, sender=VotedRank)
def update_rate(sender, instance=None, **kwargs):

    wallrank = WallRank.objects.get(id=instance.wall_rank.id)
    wallrank.rank = VotedRank.objects.filter(wall_rank=wallrank).aggregate(Avg("rank"))[
        "rank__avg"
    ]
    wallrank.voters = VotedRank.objects.filter(wall_rank=wallrank).count()
    wallrank.save()
