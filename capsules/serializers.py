import json
from rest_framework import serializers
from .models import Capsule, Images, Videos, GeminiMessage
from django.core.files.images import get_image_dimensions
from likes.models import Like


class GeminiMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeminiMessage
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    gemini_messages = GeminiMessageSerializer(many=True, required=False)

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError("Image size can't exceed 2MB")
        width, height = get_image_dimensions(value)
        if width > 4096:
            raise serializers.ValidationError(
                "Image width can't exceed 4096px")
        if height > 4096:
            raise serializers.ValidationError(
                "Image height can't exceed 4096px")
        return value

    class Meta:
        model = Images
        fields = ["id", "url", "date_taken", "gemini_messages"]

    def create(self, validated_data):
        gemini_messages_data = validated_data.pop('gemini_messages', [])
        image = Images.objects.create(**validated_data)
        for gemini_message_data in gemini_messages_data:
            GeminiMessage.objects.create(image=image, **gemini_message_data)
        return image


class VideoSerializer(serializers.ModelSerializer):
    gemini_messages = GeminiMessageSerializer(many=True, required=False)

    def validate_video(self, value):
        if value.size > 1024 * 1024 * 10:
            raise serializers.ValidationError("Video size can't exceed 10MB")
        return value

    class Meta:
        model = Videos
        fields = ["id", "url", "date_taken", "gemini_messages"]

    def create(self, validated_data):
        gemini_messages_data = validated_data.pop('gemini_messages', [])
        video = Videos.objects.create(**validated_data)
        for gemini_message_data in gemini_messages_data:
            GeminiMessage.objects.create(video=video, **gemini_message_data)
        return video


class CapsuleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    images = ImageSerializer(many=True, required=False)
    videos = VideoSerializer(many=True, required=False)
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()

    uploaded_images = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False
    )
    uploaded_images_metadata = serializers.CharField(
        write_only=True, required=False)
    uploaded_videos = serializers.ListField(
        child=serializers.FileField(), write_only=True, required=False
    )
    uploaded_videos_metadata = serializers.CharField(
        write_only=True, required=False)

    def get_is_owner(self, obj):
        return self.context["request"].user == obj.owner

    def get_like_id(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, capsule=obj).first()
            return like.id if like else None
        return None

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images", [])
        uploaded_images_metadata = json.loads(
            validated_data.pop("uploaded_images_metadata", "[]"))
        uploaded_videos = validated_data.pop("uploaded_videos", [])
        uploaded_videos_metadata = json.loads(
            validated_data.pop("uploaded_videos_metadata", "[]"))

        capsule = Capsule.objects.create(**validated_data)

        images = []
        for image_file, image_data in zip(
                uploaded_images, uploaded_images_metadata
        ):
            date_taken = image_data.get("date_taken")
            gemini_messages_data = image_data.get("gemini_messages", [])
            image = Images.objects.create(
                capsule=capsule, url=image_file, date_taken=date_taken
            )
            for gemini_message_data in gemini_messages_data:
                GeminiMessage.objects.create(
                    image=image, **gemini_message_data)
            images.append(image)

        videos = []
        for video_file, video_data in zip(
                uploaded_videos, uploaded_videos_metadata
        ):
            date_taken = video_data.get("date_taken")
            gemini_messages_data = video_data.get("gemini_messages", [])
            video = Videos.objects.create(
                capsule=capsule, url=video_file, date_taken=date_taken
            )
            for gemini_message_data in gemini_messages_data:
                GeminiMessage.objects.create(
                    video=video, **gemini_message_data)
            videos.append(video)

        return capsule

    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop("uploaded_images", [])
        uploaded_images_metadata = json.loads(
            validated_data.pop("uploaded_images_metadata", "[]"))
        uploaded_videos = validated_data.pop("uploaded_videos", [])
        uploaded_videos_metadata = json.loads(
            validated_data.pop("uploaded_videos_metadata", "[]"))

        instance.title = validated_data.get("title", instance.title)
        instance.message = validated_data.get("message", instance.message)
        instance.release_date = validated_data.get(
            "release_date", instance.release_date)
        instance.save()

        images = []
        for image_file, image_data in zip(
                uploaded_images, uploaded_images_metadata
        ):
            date_taken = image_data.get("date_taken")
            gemini_messages_data = image_data.get("gemini_messages", [])
            image = Images.objects.create(
                capsule=instance, url=image_file, date_taken=date_taken
            )
            for gemini_message_data in gemini_messages_data:
                GeminiMessage.objects.create(
                    image=image, **gemini_message_data)
            images.append(image)

        videos = []
        for video_file, video_data in zip(
                uploaded_videos, uploaded_videos_metadata
        ):
            date_taken = video_data.get("date_taken")
            gemini_messages_data = video_data.get("gemini_messages", [])
            video = Videos.objects.create(
                capsule=instance, url=video_file, date_taken=date_taken
            )
            for gemini_message_data in gemini_messages_data:
                GeminiMessage.objects.create(
                    video=video, **gemini_message_data)
            videos.append(video)

        return instance

    class Meta:
        model = Capsule
        fields = [
            "id",
            "owner",
            "title",
            "message",
            "release_date",
            "created_on",
            "updated_on",
            "is_owner",
            "profile_id",
            "images",
            "videos",
            "uploaded_images",
            "uploaded_images_metadata",
            "uploaded_videos",
            "uploaded_videos_metadata",
            "like_id",
            "likes_count",
        ]
