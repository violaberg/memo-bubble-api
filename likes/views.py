from rest_framework import generics, permissions
from memo_bubble.permissions import IsOwnerOrReadOnly
from .models import Like
from .serializers import LikeSerializer
from notifications.signals import notify
from capsules.models import Capsule


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
        like = serializer.save(owner=self.request.user)
        capsule = like.capsule
        notify.send(
            self.request.user,
            recipient=Capsule.owner,
            verb='liked your capsule',
            target=capsule
        )


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Concrete view for retrieving, updating or deleting a model instance.
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [
        IsOwnerOrReadOnly
    ]
