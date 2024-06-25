from django.contrib import admin
from .models import Capsule, Image, Video, GeminiMessage

admin.site.register(Capsule)
admin.site.register(Image)
admin.site.register(Video)
admin.site.register(GeminiMessage)
