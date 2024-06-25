from django.db import models
from django.contrib.auth.models import User


class Capsule(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    message = models.TextField()
    release_date = models.DateTimeField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.owner}'s Capsule: {self.title}"


class Image(models.Model):
    capsule = models.ForeignKey(
        Capsule, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='memo-bubble/images/')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = "Images"

    def __str__(self):
        return f"{self.capsule.title} Image"


class Video(models.Model):
    capsule = models.ForeignKey(
        Capsule, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='memo-bubble/videos/')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = "Videos"

    def __str__(self):
        return f"{self.capsule.title} Video"


class GeminiMessage(models.Model):
    capsule = models.ForeignKey(
        Capsule, related_name='gemini_messages', on_delete=models.CASCADE)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = "Gemini Messages"

    def __str__(self):
        return f"{self.capsule.title} Gemini Fact Message"
