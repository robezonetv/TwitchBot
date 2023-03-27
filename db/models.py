import sys
from django.db import models

# Sample User model
class User(models.Model):
    name = models.CharField(max_length=50, default="Dan")

    def __str__(self):
        return self.name

class TwitchUsers(models.Model):
    twitch_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    msg_count = models.IntegerField(default=0)
    last_msg_timestamp = models.IntegerField(default=0)
    follow_date = models.IntegerField(default=0)
    unfollow_date = models.IntegerField(default=0)
    unfollow = models.IntegerField(default=0)
    notified_follow = models.IntegerField(default=0)
    first_watch = models.IntegerField(default=0)
    watch_minutes = models.IntegerField(default=0)
    watch_last_check = models.IntegerField(default=0)
    pixels = models.IntegerField(default=0)

class TwitchIdToUser(models.Model):
    twitch_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
