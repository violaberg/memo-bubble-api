from rest_framework import generics, filters, permissions, status
from django_filters import rest_framework as filter
from .models import Capsule, Images, Videos, GeminiMessage
from .serializers import CapsuleSerializer, ImageSerializer, VideoSerializer, GeminiMessageSerializer
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from memo_bubble.permissions import IsAdminUserOrReadOnly, IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
import boto3
import json
from botocore.exceptions import NoCredentialsError, ClientError
from django.http import JsonResponse


class CapsuleFilter(filter.FilterSet):

    min_date = filter.DateFilter(field_name='release_date', lookup_expr='gte')
    max_date = filter.DateFilter(field_name='release_date', lookup_expr='lte')

    class Meta:
        model = Capsule
        fields = {
            'owner': ['exact'],
            'release_date': ['exact'],
        }


class CapsuleList(generics.ListCreateAPIView):
    queryset = Capsule.objects.annotate(
        likes_count=Count('likes', distinct=True),
        capsule_count=Count("owner__capsule")).order_by("-capsule_count")
    serializer_class = CapsuleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_class = CapsuleFilter

    filterset_fields = [
        # 'owner__followed__owner__profile',
        'likes__owner',
        'owner',
        'release_date',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CapsuleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Capsule.objects.all()
    serializer_class = CapsuleSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ImageList(generics.ListCreateAPIView):
    def get_queryset(self):
        return Images.objects.filter(capsule=self.kwargs["pk"])

    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class VideoList(generics.ListCreateAPIView):
    def get_queryset(self):
        return Videos.objects.filter(capsule=self.kwargs["pk"])

    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


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
    permission_classes = [IsAuthenticatedOrReadOnly]


class ImageDelete(generics.RetrieveDestroyAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self):
        # Retrieve the specific image by its ID
        image_id = self.kwargs["image_id"]
        return generics.get_object_or_404(Images, id=image_id)


class VideoDelete(generics.RetrieveDestroyAPIView):
    queryset = Videos.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self):
        # Retrieve the specific video by its ID
        video_id = self.kwargs["video_id"]
        return generics.get_object_or_404(Videos, id=video_id)


class GeminiMessageDelete(generics.RetrieveDestroyAPIView):
    queryset = GeminiMessage.objects.all()
    serializer_class = GeminiMessageSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self):
        # Retrieve the specific gemini message by its ID
        gemini_message_id = self.kwargs["gemini_message_id"]
        return generics.get_object_or_404(GeminiMessage, id=gemini_message_id)


class InitiateMultipartUpload(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):
        file_name = request.data.get("file_name")
        if not file_name or not isinstance(file_name, str):
            return Response({"error": "Missing or invalid file name"}, status=status.HTTP_400_BAD_REQUEST)

        s3_client = boto3.client('s3',
                                 aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                 aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                                 region_name=settings.AWS_S3_REGION_NAME)

        try:
            response = s3_client.create_multipart_upload(
                Bucket=settings.AWS_STORAGE_BUCKET_NAME,
                Key=file_name
            )
            return JsonResponse({'uploadId': response['UploadId']})
        except NoCredentialsError:
            return JsonResponse({'error': 'Credentials not available'}, status=403)
        except ClientError as e:
            return JsonResponse({'error': str(e)}, status=500)


class GeneratePresignedUrl(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        file_name = request.query_params.get("file_name")
        part_number = request.query_params.get("part_number")
        upload_id = request.query_params.get("upload_id")

        if not file_name or not isinstance(file_name, str):
            return Response({"error": "Missing or invalid file name"}, status=status.HTTP_400_BAD_REQUEST)
        if not part_number:
            return Response({"error": "Missing part number"}, status=status.HTTP_400_BAD_REQUEST)
        if not upload_id:
            return Response({"error": "Missing upload ID"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            part_number = int(part_number)
        except (TypeError, ValueError):
            return Response({"error": "Invalid part number"}, status=status.HTTP_400_BAD_REQUEST)

        s3_client = boto3.client('s3',
                                 aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                 aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                                 region_name=settings.AWS_S3_REGION_NAME)

        try:
            presigned_url = s3_client.generate_presigned_url(
                ClientMethod='upload_part',
                Params={
                    'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
                    'Key': file_name,
                    'UploadId': upload_id,
                    'PartNumber': part_number
                },
                ExpiresIn=3600
            )
            return Response({"url": presigned_url}, status=status.HTTP_200_OK)
        except NoCredentialsError:
            return Response({"error": "Credentials not available"}, status=status.HTTP_400_BAD_REQUEST)
        except ClientError as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CompleteMultipartUpload(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        s3_client = boto3.client('s3',
                                 aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                 aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                                 region_name=settings.AWS_S3_REGION_NAME)

        upload_id = request.data.get('uploadId')
        parts = request.data.get('parts')
        file_name = request.data.get('fileName')

        if not upload_id or not parts or not file_name:
            return JsonResponse({'error': 'Missing parameters'}, status=400)

        try:
            result = s3_client.complete_multipart_upload(
                Bucket=settings.AWS_STORAGE_BUCKET_NAME,
                Key=file_name,
                UploadId=upload_id,
                MultipartUpload={'Parts': parts}
            )
            return JsonResponse(result)
        except NoCredentialsError:
            return JsonResponse({'error': 'Credentials not available'}, status=403)
        except ClientError as e:
            return JsonResponse({'error': str(e)}, status=500)


class SaveVideoMetadata(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
