from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_extensions.db.models import TimeStampedModel

User = get_user_model()


class UserCredit(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="credit")
    credit = models.PositiveIntegerField(default=0)

    @receiver(post_save, sender=User)
    def create_user_credit(sender, instance, created, **kwargs):
        if created:
            UserCredit.objects.create(user=instance)

    def __str__(self):
        return self.user.username
