"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import home_view
from django.contrib.auth.views import LogoutView, LoginView
from user.views import register_view, profile_view
from django.conf.urls.static import static
from django.conf import settings
from home.views import (
    PostListView, PostDetailView,
    PostCreateView, PostDeleteView,
    PostUpdateView, UserPostListView)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home_view, name='home'),
    path('', PostListView.as_view(), name='home'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/',
         LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('', include('home.urls')),

    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('postDelete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('postUpdate/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('post/new/', PostCreateView.as_view(), name='new-post'),
    path('post/<str:username>/', UserPostListView.as_view(), name='user-post'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
