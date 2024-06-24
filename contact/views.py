from .models import ContactForm
from .serializers import ContactFormSerializer
from rest_framework import generics, permissions, filters, status
from django_filters import rest_framework as filter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
import os

ADMIN_EMAIL = os.environ.get("EMAIL_ADDRESS")


class ContactFormFilter(filter.FilterSet):
    """
    This class is used to filter the contact form by name, email, subject
    and created_at
    It also allows to filter the contact form by the date it was created
    """

    min_created_on = filter.DateFilter(
        field_name="created_on", lookup_expr="gte")
    max_created_on = filter.DateFilter(
        field_name="created_on", lookup_expr="lte")

    class Meta:
        model = ContactForm
        fields = ["first_name", "last_name", "email",
                  "phone_number", "subject", "created_on"]


class ContactFormCreate(generics.CreateAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer

    def perform_create(self, serializer):
        subject = self.request.data.get('subject')
        first_name = self.request.data.get('first_name')
        last_name = self.request.data.get('last_name')
        message = self.request.data.get('message')
        phone_number = self.request.data.get('phone_number')
        email = self.request.data.get('email')

        serializer.save()
        send_mail(
            subject=subject,
            message=f"New contact form from {first_name} {last_name}.\n\n"
                    f"Message: {message}\n\n"
                    f"Phone number: {phone_number}\nEmail: {email}",
            from_email=email,
            recipient_list=[ADMIN_EMAIL],
            fail_silently=False,
        )


class ContactFormList(generics.ListAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ContactFormFilter
    search_fields = [
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "subject",
        "created_on",
    ]


class ContactFormDetail(generics.RetrieveAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
    permission_classes = [permissions.IsAdminUser]
