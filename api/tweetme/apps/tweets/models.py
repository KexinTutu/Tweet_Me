import random

from django.conf import settings
from django.db import models

from tweetme.apps.utils.time_helpers import utc_now

User = settings.AUTH_USER_MODEL


class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(
        User,
        related_name="like_users",
        blank=True,
        through=TweetLike
    )
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.content

    @property
    def hours_to_now(self):
        return (utc_now() - self.created_at).seconds // 3600
