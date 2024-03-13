"""
URL configuration for django_project project.

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
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from users.views import logout_view, profile_view
from django.conf import settings
from django.conf.urls.static import static

# LoginView.get_template_names()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('register/', include('users.urls')),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.
