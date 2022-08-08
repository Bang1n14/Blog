from django.shortcuts import render
from .models import Post
from django.views.generic.base import View


class PostView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'posts/post.html', {'post_list': posts[::-1]})


class PostAbout(View):
    def get(self, request):
        return render(request, 'posts/about.html')


class PostContact(View):
    def get(self, request):
        return render(request, 'posts/contact.html')
