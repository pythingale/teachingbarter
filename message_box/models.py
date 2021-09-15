from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_extensions.db.models import TimeStampedModel

User = get_user_model()


class MessageBox(TimeStampedModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="message_box"
    )

    @receiver(post_save, sender=User)
    def create_message_box(sender, instance, created, **kwargs):
        if created:
            MessageBox.objects.create(user=instance)

    def __str__(self):
        return self.user.username


class Message(TimeStampedModel):
    message = models.CharField(max_length=150)
    sender = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="message_sender",
    )
    message_box = models.ForeignKey(
        MessageBox, on_delete=models.CASCADE, related_name="message"
    )

    def __str__(self):
        return self.message
