from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_extensions.db.models import TimeStampedModel

User = get_user_model()


class Transaction(TimeStampedModel):
    credit_sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="credit_sender"
    )
    credit_receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="credit_receiver"
    )
    amount = models.PositiveIntegerField()
    description = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return str(self.amount)


class UserCredit(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="credit")
    credit = models.PositiveIntegerField(default=0)

    @receiver(post_save, sender=User)
    def create_user_credit(sender, instance, created, **kwargs):
        if created:
            UserCredit.objects.create(user=instance)

    @receiver(post_save, sender=Transaction)
    def do_transaction(sender, instance, created, **kwargs):
        if created:
            sender_user = UserCredit.objects.get(user=instance.credit_sender)
            sender_user.credit -= instance.amount
            sender_user.save()
            receiver_user = UserCredit.objects.get(user=instance.credit_receiver)
            receiver_user.credit += instance.amount
            receiver_user.save()

    def __str__(self):
        return self.user.username
