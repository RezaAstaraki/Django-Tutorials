from django.db import models
from django.contrib.auth.models import User
import PIL


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', default='default.jpg')

    def __str__(self):
        return f'profile : {self.user}'

    # def save(self):
    #     super.save()

    #     img = open(self.image.url)
    #     print(img)
