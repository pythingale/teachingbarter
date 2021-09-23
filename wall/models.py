from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_extensions.db.models import TimeStampedModel
from stdimage import StdImageField

from skills.models import Skill

User = get_user_model()


class UserWall(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="wall")
    description = models.CharField(default="", max_length=300)
    skills = models.ManyToManyField(Skill)
    avatar = StdImageField(
        upload_to="./media/image/cover",
        blank=True,
        variations={
            "large": (800, 400),
            "thumbnail": (100, 100, True),
        },
        delete_orphans=True,
    )

    def get_username(self):
        return self.user.username

    def get_rank(self):
        return self.wall_rank.rank

    def get_vote_numbers(self):
        return self.wall_rank.voters

    def get_voters(self):
        return self.wall_rank.votedrank.all()

    @receiver(post_save, sender=User)
    def create_user_wall(sender, instance, created, **kwargs):
        if created:
            UserWall.objects.create(user=instance)

    def __str__(self):
        return self.user.username
