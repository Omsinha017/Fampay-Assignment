from django.contrib import admin
from .models import Video, VideoThumnails, YoutubeAPIKeys

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Video._meta.fields]
	search_fields = ('publish_date_time', 'video_id', 'channel_id', 'title', 'id')

@admin.register(VideoThumnails)
class VideoThumbNailAdmin(admin.ModelAdmin):
	list_display = [field.name for field in VideoThumnails._meta.fields]
	search_fields = ('video__title', 'video__channel_id', 'video__video_id', 'video__publish_date_time', 'id')

@admin.register(YoutubeAPIKeys)
class APIKeyAdmin(admin.ModelAdmin):
	list_display = [field.name for field in YoutubeAPIKeys._meta.fields]