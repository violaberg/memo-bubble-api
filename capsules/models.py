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


class Images(models.Model):
    capsule = models.ForeignKey(
        Capsule, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='memo-bubble/images/')
    date_taken = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-date_taken']
        verbose_name_plural = "Images"

    def __str__(self):
        owner = self.capsule.owner
        capsule = self.capsule.title
        date = self.date_taken.strftime("%d-%m-%Y")
        return f"{owner}'s capsule {capsule} Image {self.id}, {date}"


class Videos(models.Model):
    capsule = models.ForeignKey(
        Capsule, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='memo-bubble/videos/')
    date_taken = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-date_taken']
        verbose_name_plural = "Videos"

    def __str__(self):
        owner = self.capsule.owner
        capsule = self.capsule.title
        date = self.date_taken.strftime("%d-%m-%Y")
        return f"{owner}'s capsule {capsule} Video {self.id}, {date}"


class GeminiMessage(models.Model):
    image = models.ForeignKey(Images, related_name='gemini_messages',
                              on_delete=models.CASCADE, null=True, blank=True)
    video = models.ForeignKey(Videos, related_name='gemini_messages',
                              on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = "Gemini Messages"

    def __str__(self):
        return f"{self.video or self.image}: {self.message[:50]}..."
