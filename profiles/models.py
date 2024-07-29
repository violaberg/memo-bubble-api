from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    """
    Represents a user profile.
    """

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email_address = models.EmailField(max_length=255, blank=True)
    phone = PhoneNumberField(blank=True)
    image = models.ImageField(
        upload_to="memo-bubble/profile_images",
        default="https://memo-bubble-app.s3.eu-west-1.amazonaws.com/media/memo-bubble/placeholder/placeholder.png", blank=True
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
