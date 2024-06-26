from django.urls import path
from .views import CapsuleList, CapsuleDetail

urlpatterns = [
    path('capsules/', CapsuleList.as_view(), name='capsule-list'),
    path('capsules/<int:pk>/', CapsuleDetail.as_view(), name='capsule-detail'),
]
