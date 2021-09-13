from __future__ import absolute_import, unicode_literals

from config import celery_app

# from celery import Celery
from .models import UserCredit

# celery = Celery('tasks', broker='amqp://rabbitmq')


@celery_app.task
def increase():
    query = UserCredit.objects.all()
    for instance in query:
        instance.credit += 20
        instance.save()
