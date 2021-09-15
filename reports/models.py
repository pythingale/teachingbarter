from django.contrib.auth import get_user_model
from django.db import models
from django_extensions.db.models import TimeStampedModel

User = get_user_model()


class Report(TimeStampedModel):
    reported_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reported"
    )
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reporter")
    message = models.CharField(max_length=300)

    def __str__(self):
        return self.message
