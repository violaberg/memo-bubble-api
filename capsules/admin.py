from django.contrib import admin
from .models import Capsule, Images, Videos, GeminiMessage

admin.site.register(Capsule)
admin.site.register(Images)
admin.site.register(Videos)
admin.site.register(GeminiMessage)
