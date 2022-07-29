from django.shortcuts import render
from .models import Post
from django.views.generic.base import View


class PostView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'posts/post.html', {'post_list': posts})
