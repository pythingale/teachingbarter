from django.contrib import admin

from .models import Transaction, UserCredit

admin.site.register(UserCredit)
admin.site.register(Transaction)
