from django.conf import settings
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Report(TimeStampedModel):
    reported_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reported"
    )
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reporter"
    )
    message = models.CharField(max_length=300)

    def __str__(self):
        return self.message
