import json
import requests
from django.db.models import Q
from django.http import HttpRequest
from rest_framework import generics
from django.views.generic import View
from .models import Video, VideoThumnails, YoutubeAPIKeys
from .constants import *
from .response import init_response, send_200, send_201, send_400
from .pagination import YoutubeSearchListPagination
from .utils import get_video_dict_from_result, get_video_thumbnails_from_result
from .serializers import VideoSerializer

class FetchAndStoreYouTubeSearchData(View):

    def get_api_request(self, params):
        '''
        Args: Takes yotube request params as an argument
        Returns: Returns an HTTP GET request, which contains the params which is 
                 required to call the youtube search api
        '''
        request = HttpRequest()
        request.method = 'GET'
        request.GET.update(params)
        return request

    def fetch_youtube_search_data(self, query, max_results, youtube_api_key, published_after):
        '''
        Args: Takes query, max resultsm youtube_api key and published_after as an 
              argument, which are required to get the search result
        Return: Returns the search reponse in json format
        '''
        search_response = []
        SEARCH_PARAMS = {
            'part':'snippet',
            'order':'date',
            'type':'video',
            'maxResults':max_results, 
            'q':query,
            'publishedAfter':published_after.strftime('%Y-%m-%dT%H:%M:%SZ'),
            'key':youtube_api_key.key
        }
        try:
            import pdb; pdb.set_trace()
            get_youtube_search_response = requests.get(YOTUBE_SEARCH_URL, SEARCH_PARAMS)
            search_response = json.loads(get_youtube_search_response.content).get('items', [])
        except:
            youtube_api_key.status = False
            youtube_api_key.save(update_fields=['status'])
        return search_response

    def save_video_and_thumbail(self, search_result):
        '''
        Args: Take Youtube search_result in response
        Does: Add Video and it's thumbnail to 
              the db only when no video exists with the current video_id we got in response
        '''
        for search_response in search_result:
            video_data_dict = get_video_dict_from_result(search_response)
            videoId = video_data_dict.get('video_id')
            video_obj = Video.objects.filter(video_id=videoId, )
            if not video_obj:
                video_obj = Video(**video_data_dict)
                video_obj.save()
                thumbnails = get_video_thumbnails_from_result(search_response)
                thumbnails_objects_list = []
                for thumbnail in thumbnails:
                    thumbnail['video'] = video_obj
                    thumbnails_objects_list.append(VideoThumnails(**thumbnail))
                VideoThumnails.objects.bulk_create(thumbnails_objects_list)

    def get(self, request):
        '''
        Args: Takes the seach_request as argument
        Does: Call the Youtube search API and then save the reponse in the database
        '''
        params = request.GET.dict()
        query = params.get('query')
        max_search_results = params.get('max_search_results')
        youtube_api_key = params.get('youtube_api_key')
        published_after = params.get('published_after')
        search_result = self.fetch_youtube_search_data(query, max_search_results, youtube_api_key, published_after)
        self.save_video_and_thumbail(search_result)

class AddYoutubeSearchAPIKey(View):

    def __init__(self):
        self.response = init_response()

    def post(self, request):
        '''
        Args: Takes yotube api key from request
        Does: Add Youtube API key to the database, and raise error if already exists
        '''
        params = request.POST.dict()
        try:
            key = params.get('key')
            if key:
                youtube_key_obj = YoutubeAPIKeys.objects.filter(key=key)
                if youtube_key_obj:
                    self.response['res_str'] = KEY_ALREADY_EXISTS
                else:
                    self.response['res_str'] = KEY_ADDED_SUCCESSFULLY
                    return send_201(self.response)
            else:
                self.response['res_str'] = KEY_REQUIRED
        except Exception as ex:
            self.response['res_str'] = ex
        return send_400(self.response)

class SearchYoutubeVideos(generics.ListAPIView):
    serializer_class = VideoSerializer
    pagination_class = YoutubeSearchListPagination

    def get_queryset(self):
        '''
        Args: Get the query params from the GET request
        Returns: Get all the data which matches the tile or descprtion, in pagination format
        '''
        queryset = Video.objects.all()
        query = self.request.query_params.get('query', None)
        if query:
            return queryset.filter(Q(title__contains=query) | Q(description__contains=query))
        return queryset