from rest_framework import generics, filters
from .models import Capsule, Images, Videos, GeminiMessage
from .serializers import CapsuleSerializer, ImageSerializer, VideoSerializer, GeminiMessageSerializer
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from memo_bubble.permissions import IsAdminUserOrReadOnly


class CapsuleList(generics.ListCreateAPIView):
    queryset = Capsule.objects.annotate(
        capsule_count=Count("owner__capsule")).order_by("-capsule_count")
    serializer_class = CapsuleSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
