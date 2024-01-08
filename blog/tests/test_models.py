from django.test import TestCase
from django.contrib.auth import get_user_model
from blog.models import Post


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", password="12345"
        )
        cls.post = Post.objects.create(
            author=cls.user, title="Test Post", content="Just some test content"
        )

    def test_model_content(self):
        expected_author = f"{self.post.author.username}"
        expected_title = f"{self.post.title}"
        expected_content = f"{self.post.content}"
        self.assertEqual(expected_author, "testuser")
        self.assertEqual(expected_title, "Test Post")
        self.assertEqual(expected_content, "Just some test content")

    def test_post_str(self):
        post = Post.objects.get(id=1)
        expected_object_name = f"{post.title}"
        self.assertEqual(expected_object_name, str(post))
