from rest_framework import generics, permissions
from memo_bubble.permissions import IsOwnerOrReadOnly
from .models import Like
from .serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    """
    Concrete view for listing a queryset(likes)
    or creating a model instance.
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Concrete view for retrieving, updating or deleting a model instance.
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [
        IsOwnerOrReadOnly
    ]
