from rest_framework import filters, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from users.permissions import UpdateOwnStatus

from .models import UserWall
from .serializers import UserWallSerializer


class UserWallViewSet(viewsets.ModelViewSet):
    queryset = UserWall.objects.all()
    serializer_class = UserWallSerializer
    permission_classes = (UpdateOwnStatus, IsAuthenticatedOrReadOnly)
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        "user.username",
        "skills",
    )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
