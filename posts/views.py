from django.shortcuts import render


# Create your views here.
from posts.models import Post


def posts_home(request):
    posts = Post.objects.all()
    contex = {
        "posts" : posts
    }
    return render(request, 'posts.html', contex)
