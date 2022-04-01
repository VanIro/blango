from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
# Create your views here.

def index(request):
  posts = Post.objects.all()#filter(published_at__lte=timezone.now())
  
  print(timezone.now())
  return render(request, "blog/index.html", {"posts":posts})