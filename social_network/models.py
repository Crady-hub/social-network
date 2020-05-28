from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class LikeUnlike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    LIKE_UNLIKE = [
        ('like', 'Like'),
        ('unlike', 'Unlike')
    ]
    like = models.CharField(
        max_length=6, choices=LIKE_UNLIKE, default='unlike')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.post

    class Meta:
        verbose_name = 'Like/Unlike'
        verbose_name_plural = 'Likes/Unlikes'
