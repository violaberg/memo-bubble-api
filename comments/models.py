from django.db import models
from django.contrib.auth.models import User
from capsules.models import Capsule


class Comment(models.Model):
    capsule = models.ForeignKey(
        Capsule, related_name='comments', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = "comments"

    def __str__(self):
        return f"{self.comment} by {self.owner}"
