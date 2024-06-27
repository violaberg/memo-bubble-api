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


class CapsuleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Capsule.objects.all()
    serializer_class = CapsuleSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ImageList(generics.ListCreateAPIView):
    def get_queryset(self):
        return Images.objects.filter(capsule=self.kwargs["pk"])

    serializer_class = ImageSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class VideoList(generics.ListCreateAPIView):
    def get_queryset(self):
        return Videos.objects.filter(capsule=self.kwargs["pk"])

    serializer_class = VideoSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class GeminiMessageList(generics.ListCreateAPIView):
    # The gemini messages are associated with either an image or a video.
    # The image or video is associated with a capsule.
    # Therefore, the gemini messages can be fetched by the capsule id.

    def get_queryset(self):
        if "image_id" in self.kwargs:
            return GeminiMessage.objects.filter(image=self.kwargs["image_id"])
        elif "video_id" in self.kwargs:
            return GeminiMessage.objects.filter(video=self.kwargs["video_id"])

    serializer_class = GeminiMessageSerializer
    permission_classes = [IsAdminUserOrReadOnly]
