from rest_framework import serializers
from .models import Comment
from django.contrib.humanize.templatetags.humanize import naturaltime


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.profile_pic.url')
    created_on = serializers.SerializerMethodField()
    updated_on = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'capsule', 'owner', 'comment', 'created_on',
                  'updated_on', 'is_owner', 'profile_id', 'profile_image']

    def get_is_owner(self, obj):
        request = self.context['request']
        return obj.owner == request.user

    def get_created_on(self, obj):
        return naturaltime(obj.created_on)

    def get_updated_on(self, obj):
        return naturaltime(obj.updated_on)


class CommentDetailSerializer(CommentSerializer):
    post = serializers.ReadOnlyField(source='capsule.id')
