from rest_framework import serializers

from .models import Transaction, UserCredit


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "id",
            "credit_sender",
            "credit_receiver",
            "amount",
            "description",
            "created",
        ]


class UserCreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCredit
        fields = ["id", "user", "credit"]
