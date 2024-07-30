from django.urls import path
from . import views

urlpatterns = [
    path('capsules/', views.CapsuleList.as_view(), name='capsule-list'),
    path('capsules/<int:pk>/', views.CapsuleDetail.as_view(),
         name='capsule-detail'),
    path('capsules/<int:pk>/images/',
         views.ImageList.as_view(), name='image-list'),
    path('capsules/<int:pk>/videos/',
         views.VideoList.as_view(), name='video-list'),
    path('capsules/<int:pk>/images/<int:image_id>/gemini-messages/',
         views.GeminiMessageList.as_view(), name='gemini-message-list'),
    path('capsules/<int:pk>/videos/<int:video_id>/gemini-messages/',
         views.GeminiMessageList.as_view(), name='gemini-message-list'),
    path('capsules/<int:pk>/images/<int:image_id>/',
         views.ImageDelete.as_view(), name='image-delete'),
    path('capsules/<int:pk>/videos/<int:video_id>/',
         views.VideoDelete.as_view(), name='video-delete'),
    path('capsules/<int:pk>/images/<int:image_id>'
         '/gemini-messages/<int:gemini_message_id>/',
         views.GeminiMessageDelete.as_view(), name='gemini-message-delete'),
    path('initiate_multipart_upload/', views.InitiateMultipartUpload.as_view(),
         name='initiate_multiple_upload'),
    path('generate_presigned_url/', views.GeneratePresignedUrl.as_view(),
         name='generate_presigned_url'),
    path('save_video_metadata/', views.SaveVideoMetadata.as_view(),
         name='save_video_metadata'),
    path('complete_multipart_upload/', views.CompleteMultipartUpload.as_view(),
         name='complete-multipart-upload'),
     path('api/maps/place/', views.GetPlaceAutocomplete.as_view(),
          name='place-autocomplete'),
]
