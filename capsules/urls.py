from django.urls import path
from .views import CapsuleList

urlpatterns = [
    path('capsules/', CapsuleList.as_view(), name='capsule-list'),
]
