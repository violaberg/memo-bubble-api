from rest_framework import generics, permissions
from memo_bubble.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer
from notifications.signals import notify
from capsules.models import Capsule


class CommentList(generics.ListCreateAPIView):
    """
    Concrete view for listing a queryset(comments)
    or creating a model instance.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def perform_create(self, serializer):
        comment = serializer.save(owner=self.request.user)
        capsule = comment.capsule
        notify.send(
            self.request.user,
            recipient=Capsule.owner,
            verb='commented on your capsule',
            target=capsule
        )


class CommentDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a comment, update or delete it by id if you own it.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
