from rest_framework import generics, filters
from .models import Capsule, Images, Videos, GeminiMessage
from .serializers import CapsuleSerializer, ImageSerializer, VideoSerializer, GeminiMessageSerializer
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from memo_bubble.permissions import IsAdminUserOrReadOnly


class CapsuleList(generics.ListCreateAPIView):
    queryset = Capsule.objects.annotate(
        likes_count=Count('likes', distinct=True),
        capsule_count=Count("owner__capsule")).order_by("-capsule_count")
    serializer_class = CapsuleSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = [
        # 'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
    ]

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


class ImageDelete(generics.RetrieveDestroyAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_object(self):
        # Retrieve the specific image by its ID
        image_id = self.kwargs["image_id"]
        return generics.get_object_or_404(Images, id=image_id)


class VideoDelete(generics.RetrieveDestroyAPIView):
    queryset = Videos.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_object(self):
        # Retrieve the specific video by its ID
        video_id = self.kwargs["video_id"]
        return generics.get_object_or_404(Videos, id=video_id)


class GeminiMessageDelete(generics.RetrieveDestroyAPIView):
    queryset = GeminiMessage.objects.all()
    serializer_class = GeminiMessageSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_object(self):
        # Retrieve the specific gemini message by its ID
        gemini_message_id = self.kwargs["gemini_message_id"]
        return generics.get_object_or_404(GeminiMessage, id=gemini_message_id)
