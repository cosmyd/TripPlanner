from django.db import models
from django.contrib.auth.models import User


class FriendshipList(models.Model):
    owner = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'owner')
    friends = models.ManyToManyField(User, blank=True)

class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "from_user")
    to_user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "to_user")
