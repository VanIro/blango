from rest_framework import generics

from blog.api.serializers import PostSerializer, UserSerializer
from blango_auth.models import User
from blog.models import Post

class PostList(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

class UserDetail(generics.RetrieveAPIView):
  lookup_field="email"
  queryset=User.objects.all()
  serializer_class = UserSerializer