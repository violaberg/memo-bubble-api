from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.profile_pic.url')
    created_on = serializers.SerializerMethodField()
    updated_on = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'capsule', 'owner', 'comment', 'created_on', 'updated_on',
                  'is_owner', 'profile_id', 'profile_image']
        
    def get_is_owner(self, obj):
        """
        Determine if the current user is the owner of the comment.
        """
        request = self.context.get('request')
        if request and request.user:
            return obj.owner == request.user
        return False
