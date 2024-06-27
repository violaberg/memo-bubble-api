from django.urls import path
from .views import CapsuleList, CapsuleDetail, ImageList, VideoList, GeminiMessageList

urlpatterns = [
    path('capsules/', CapsuleList.as_view(), name='capsule-list'),
    path('capsules/<int:pk>/', CapsuleDetail.as_view(), name='capsule-detail'),
    path('capsules/<int:pk>/images/', ImageList.as_view(), name='image-list'),
    path('capsules/<int:pk>/videos/', VideoList.as_view(), name='video-list'),
    path('capsules/<int:pk>/images/<int:image_id>/gemini-messages/',
         GeminiMessageList.as_view(), name='gemini-message-list'),
    path('capsules/<int:pk>/videos/<int:video_id>/gemini-messages/',
         GeminiMessageList.as_view(), name='gemini-message-list'),
]
