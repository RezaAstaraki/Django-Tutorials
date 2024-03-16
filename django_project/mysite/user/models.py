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


class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    post_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    post_content = models.TextField()

    # class Meta:
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    def __str__(self):
        return f'POST : {self.user} : {self.title}'

        # def get_absolute_url(self):
        #     return reverse("_detail", kwargs={"pk": self.pk})
