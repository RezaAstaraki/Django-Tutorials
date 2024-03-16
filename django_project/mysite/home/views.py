from django.shortcuts import render
from user.models import Post
from django.views.generic import (
    ListView, DeleteView,
    DetailView, UpdateView)
from user.models import Post


# Create your views here.


def home_view(request):

    posts = Post.objects.all()
    context = {'posts': posts}
    print('****************')
    print(posts.first()._meta.get_fields())
    print('****************')

    return render(request, 'home/home.html', context=context)


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = "home/home.html"


def about_view(request):
    return render(request, 'home/about.html')
