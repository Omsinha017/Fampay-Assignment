from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
	path('v1/get_videos/', FetchAndStoreYouTubeSearchData.as_view()),
	path('v1/add_key/', csrf_exempt(AddYoutubeSearchAPIKey.as_view())),
	path('v1/search_videos/', SearchYoutubeVideos.as_view()),
]
