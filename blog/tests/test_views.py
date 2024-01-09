from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from blog.models import Post


class PostAPITestCase(APITestCase):
    def setUp(self):
        self.moderator_user = get_user_model().objects.create_user(
            username="moderatoruser",
            email="moderator@example.com",
            password="testpassword",
            is_moderator=True,
        )

        self.client.force_authenticate(user=self.moderator_user)

        self.post = Post.objects.create(
            author=self.moderator_user, title="Test Post", content="Test Content"
        )

    def test_create_post(self):
        url = reverse("blog:post-list")
        data = {"title": "New Post", "content": "Content of the new post"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(Post.objects.get(id=2).title, "New Post")

    def test_get_post_list(self):
        url = reverse("blog:post-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)

    def test_update_post(self):
        url = reverse("blog:post-detail", kwargs={"pk": self.post.pk})
        data = {"title": "Updated Post", "content": "Updated content"}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, "Updated Post")

    def test_delete_post(self):
        url = reverse("blog:post-detail", kwargs={"pk": self.post.pk})
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            Post.objects.filter(pk=self.post.pk).exists()
        )
