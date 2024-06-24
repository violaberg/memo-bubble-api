from django.urls import path
from .views import ContactFormList, ContactFormDetail, ContactFormCreate


urlpatterns = [
    path("contact/", ContactFormCreate.as_view(), name="contact-form-list"),
    path("contact_list/", ContactFormList.as_view()),
    path("contact_list/<int:pk>/", ContactFormDetail.as_view()),
]
