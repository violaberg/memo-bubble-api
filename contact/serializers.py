from rest_framework import serializers
from .models import ContactForm
import os

ADMIN_EMAIL = os.environ.get("EMAIL_ADDRESS")


class ContactFormSerializer(serializers.ModelSerializer):
    """
    Contact form serializer.
    """

    class Meta:
        model = ContactForm
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "subject",
            "message",
            "created_on",
        ]

        extra_kwargs = {
            "first_name": {
                "error_messages": {"blank":  "This field is required"}
            },
            "last_name": {
                "error_messages": {"blank": "This field is required"}
            },
            "email": {
                "error_messages": {"blank": "This field is required"}
            },
            "phone_number": {
                "error_messages": {"blank": "This field is required"}
            },
            "subject": {
                "error_messages": {"blank": "This field is required"}
            },
            "message": {
                "error_messages": {"blank": "This field is required"}
            },
        }

        read_only_fields = ["id", "created_on"]

    def create(self, validated_data):
        """
        Creates contact form and send it via email to the admin.
        """
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        email = validated_data["email"]
        phone_number = validated_data["phone_number"]
        subject = validated_data["subject"]
        message = validated_data["message"]

        contact = ContactForm.objects.create(
            first_name=first_name, last_name=last_name, email=email,
            phone_number=phone_number, subject=subject, message=message
        )

        return contact
