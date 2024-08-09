from rest_framework import generics, permissions
from memo_bubble.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Comment
from .serializers import CommentSerializer
from notifications.signals import notify


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

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['comment', 'owner']

    def perform_create(self, serializer):
        comment = serializer.save(owner=self.request.user)
        capsule = comment.capsule
        owner = capsule.owner
        notify.send(
            self.request.user,
            recipient=owner,
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
