"""Serializers for the blog app."""

from rest_framework import serializers

from blog.models import Post
from users.models import User


class PostSerializer(serializers.ModelSerializer):
    """Serializer for the Post model."""

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'created_at',
            'updated_at',
        ]

    def to_representation(self, instance: Post) -> dict:
        """Custom representation for the Post model."""
        representation = super(PostSerializer, self).to_representation(instance)
        if (
            'request' in self.context
            and self.context['request'].method == 'GET'
        ):
            representation['author'] = UserSerializer(instance.author).data
        return representation


class PostListSerializer(serializers.ModelSerializer):
    """Serializer for listing Post objects."""

    author_username = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author_username', 'title']

    def get_author_username(self, obj: Post) -> str:
        """Custom method to get the author's username."""
        return obj.author.username


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model."""

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_moderator']
