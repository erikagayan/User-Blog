from rest_framework import viewsets, mixins

from blog.models import Post
from blog.serializers import PostListSerializer, PostSerializer
from rest_framework.permissions import IsAuthenticated
from blog.permissions import IsStaffOrReadOnly


class PostViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsStaffOrReadOnly]

    def get_serializer_class(self):
        if self.action == "list":
            return PostListSerializer
        return PostSerializer

    def get_serializer_context(self):
        return {'request': self.request}

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsStaffOrReadOnly]
        return [permission() for permission in permission_classes]
