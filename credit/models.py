from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_extensions.db.models import TimeStampedModel


class UserCredit(TimeStampedModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="credit"
    )
    Credit = models.PositiveIntegerField(default=0)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_user_credit(sender, instance, created, **kwargs):
        if created:
            UserCredit.objects.create(user=instance)

    def __str__(self):
        return self.user.username
