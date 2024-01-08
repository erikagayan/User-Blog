from rest_framework import serializers
from blog.models import Post
from users.models import User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "created_at",
            "updated_at",
        ]

    def to_representation(self, instance):
        representation = super(PostSerializer, self).to_representation(instance)
        if "request" in self.context and self.context["request"].method in ["GET"]:
            representation["author"] = UserSerializer(instance.author).data
        return representation


class PostListSerializer(serializers.ModelSerializer):
    author_username = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["id", "author_username", "title"]

    def get_author_username(self, obj):
        return obj.author.username


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "is_moderator"]
