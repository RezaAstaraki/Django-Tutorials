from django.shortcuts import render
from user.models import Post

# Create your views here.


def home_view(request):

    posts = Post.objects.all()
    context = {'posts': posts}
    print('****************')
    print(posts.first()._meta.get_fields())
    print('****************')

    return render(request, 'home/home.html', context=context)


def about_view(request):
    return render(request, 'home/about.html')
