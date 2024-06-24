from django.db import models
from django.core.validators import EmailValidator
from phonenumber_field.modelfields import PhoneNumberField


class ContactForm(models.Model):
    """
    Contact model that allows users to contact the site owner.
    """

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, validators=[EmailValidator()])
    phone_number = PhoneNumberField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}'s message"
