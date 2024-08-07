from django.db import models
from django.conf import settings
from django.utils import timezone


class Notification(models.Model):
    TYPES = (
        ('like', 'Like'),
        ('comment', 'Comment'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_notifications')
    type = models.CharField(max_length=20, choices=TYPES)
    content = models.TextField()
    is_seen = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user} - {self.type} - {self.is_seen}"