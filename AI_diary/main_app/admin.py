from django.contrib import admin
from .models import UserProfile, DiaryEntry, Image, Statistics

admin.site.register(UserProfile)
admin.site.register(DiaryEntry)
admin.site.register(Image)
admin.site.register(Statistics)
