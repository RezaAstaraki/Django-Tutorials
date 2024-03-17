from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from user.models import Post
from django.views.generic import (
    ListView,
    DeleteView,
    DetailView,
    UpdateView,
    CreateView,

)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
    ListView.ordering = ['-pk']
    paginate_by = 5
    # print('****************')
    # print('****************')


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "home/new-post.html"
    fields = ['title', 'post_content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        # print('****--------------------------')
        # print('self.request.user', self.request.user)
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post

    template_name = "home/new-post.html"
    fields = ['title', 'post_content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post.user == self.request.user:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        if post.user == self.request.user:
            return True
        else:
            return False
    # template_name = ".html"


# print(Post._meta.get_fields())


class PostDetailView(DetailView):
    model = Post
    template_name = "home/post-detail.html"


def about_view(request):
    return render(request, 'home/about.html')
