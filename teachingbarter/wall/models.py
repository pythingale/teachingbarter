from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_extensions.db.models import TimeStampedModel
from skills.models import Skill
from stdimage import StdImageField


class UserWall(TimeStampedModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="wall"
    )
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

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_user_wall(sender, instance, created, **kwargs):
        if created:
            UserWall.objects.create(user=instance)

    def __str__(self):
        return self.user.username
