from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.URLField(blank=True)
    # Users this user follows (one-way follow)
    following = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers", blank=True
    )

    def __str__(self):
        return self.username
