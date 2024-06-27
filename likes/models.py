from django.db import models
from django.contrib.auth.models import User
from capsules.models import Capsule


class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    capsule = models.ForeignKey(
        Capsule, on_delete=models.CASCADE, related_name='likes'
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ['owner', 'capsule']

    def __str__(self):
        return f'{self.owner} likes {self.capsule}'
