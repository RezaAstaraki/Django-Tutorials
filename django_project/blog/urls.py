from django.urls import path
from . import views

urlpatterns = [
    path('',view=views.home,name='blog-home'),
    path('about/',view=views.about,name='blog-about'),
]
