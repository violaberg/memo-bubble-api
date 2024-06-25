from rest_framework import serializers
from .models import Capsule, Image, Video, GeminiMessage
from django.core.files.images import get_image_dimensions


class ImageSerializer(serializers.ModelSerializer):
    def validate_images(self, value):
        for image in value:
            if image.size > 1024 * 1024 * 2:
                raise serializers.ValidationError(
                    "Image size can't exceed 2MB")
            width, height = get_image_dimensions(image)
            if width > 4096:
                raise serializers.ValidationError(
                    "Image width can't exceed 4096px")
            if height > 4096:
                raise serializers.ValidationError(
                    "Image height can't exceed 4096px")
        return value

    class Meta:
        model = Image
        fields = ['id', 'image', 'created_on', 'updated_on']


class VideoSerializer(serializers.ModelSerializer):
    def validate_videos(self, value):
        for video in value:
            if video.size > 1024 * 1024 * 10:
                raise serializers.ValidationError(
                    "Video size can't exceed 10MB")
        return value

    class Meta:
        model = Video
        fields = '__all__'


class GeminiMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeminiMessage
        fields = '__all__'


class CapsuleSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="agent_name.profile.id")
    images = ImageSerializer(many=True, read_only=True)
    videos = VideoSerializer(many=True, read_only=True)
    gemini_messages = GeminiMessageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(), write_only=True,
        validators=[ImageSerializer().validate_images], required=False)
    uploaded_videos = serializers.ListField(
        child=serializers.FileField(), write_only=True,
        validators=[VideoSerializer().validate_videos], required=False)
    uploaded_gemini_messages = serializers.ListField(
        child=serializers.CharField(), write_only=True)

    def get_is_owner(self, obj):
        return self.context['request'].user == obj.owner

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        uploaded_videos = validated_data.pop('uploaded_videos', [])
        uploaded_gemini_messages = validated_data.pop(
            'uploaded_gemini_messages', [])
        capsule = Capsule.objects.create(**validated_data)
        for uploaded_image in uploaded_images:
            Image.objects.create(capsule=capsule, image=uploaded_image)
        for uploaded_video in uploaded_videos:
            Video.objects.create(capsule=capsule, video=uploaded_video)
        for uploaded_gemini_message in uploaded_gemini_messages:
            GeminiMessage.objects.create(
                capsule=capsule, message=uploaded_gemini_message)
        return capsule

    class Meta:
        model = Capsule
        fields = '__all__'
