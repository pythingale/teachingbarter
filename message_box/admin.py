from django.contrib import admin

from .models import Message, MessageBox

admin.site.register(MessageBox)
admin.site.register(Message)
