from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateField(default=timezone.now)


class LikeUnlike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    LIKE_UNLIKE = [
        ('like', 'Like'),
        ('unlike', 'Unlike')
    ]
    like = models.CharField(max_length=6, choices=LIKE_UNLIKE)
    date = models.DateField(auto_now=True)