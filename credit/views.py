from django.contrib.auth import get_user_model
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Transaction, UserCredit
from .serializers import TransactionSerializer, UserCreditSerializer

# from rest_framework.exceptions import PermissionDenied
# from rest_framework.permissions import IsAdminUser, IsAuthenticated


# from rest_framework.filters import OrderingFilter


User = get_user_model()


class UserCreditViewSet(viewsets.ModelViewSet):

    queryset = UserCredit.objects.all()
    serializer_class = UserCreditSerializer


class TransactionViewSet(viewsets.ModelViewSet):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request, *args, **kwargs):
        post_data = request.data
        post_data._mutable = True
        post_data["credit_sender"] = str(request.user.id)
        serializer = TransactionSerializer(data=post_data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
