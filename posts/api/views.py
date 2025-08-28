from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet

from ..models import Post
from .serializers import PostsSerializer


class PostsViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer


def index(request):
    return HttpResponse("Hello, world. You're at jamie's coaching site.")
