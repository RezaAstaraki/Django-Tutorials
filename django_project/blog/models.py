from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


# posts = [
#     {
#         'author': author,
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2018'
#     },
#     {
#         'author': author,
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 28, 2018'
#     }
# ]
# jj = Posts.objects.bulk_create(posts)
# Posts.objects.create({'author': author,'title': 'Blog Post 2','content': 'Second post content','date_posted': 'August 28, 2018'})
#  Posts.objects.create(author= author,title='Blog Post 2',content= 'Second post content')
