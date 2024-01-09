from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from blog.models import Post
from blog.serializers import PostSerializer, PostListSerializer


class PostSerializerTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="12345", email="user@example.com"
        )
        self.post = Post.objects.create(
            author=self.user, title="Test Post", content="Just some test content"
        )

    def test_post_serializer(self):
        serializer = PostSerializer(instance=self.post)
        data = serializer.data
        self.assertEqual(
            set(data.keys()),
            {"id", "title", "content", "created_at", "updated_at"},
        )
        self.assertEqual(data["title"], "Test Post")
        self.assertEqual(data["content"], "Just some test content")

    def test_post_list_serializer(self):
        serializer = PostListSerializer(instance=self.post)
        data = serializer.data
        self.assertEqual(set(data.keys()), {"id", "author_username", "title"})
        self.assertEqual(data["title"], "Test Post")
        self.assertEqual(data["author_username"], self.user.username)
