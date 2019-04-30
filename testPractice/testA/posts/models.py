from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=140, default='')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')



