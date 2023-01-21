from datetime import datetime
from .models import YoutubeAPIKeys

def get_date_time_object_from_string(date_time_string):
    '''
    Args: Takes date_time_string as argument
    Return: Returns a datetime object
    '''
    return datetime.strptime(date_time_string.replace('T', ' ').replace('Z',''),'%Y-%m-%d %H:%M:%S')

def get_video_dict_from_result(search_response):
    '''
    Args: Takes Youtube Search Response
    Return: Formatted video dictionary
    '''
    return {
        'title': search_response.get("snippet",{}).get("title",''),
        'description': search_response.get("snippet",{}).get('description',''),
        'video_id': search_response.get('id',{}).get('videoId',''),
        'channel_id': search_response.get("snippet",{}).get('channelId',''),
        'channel_name': search_response.get("snippet",{}).get('channelTitle',''),
        'publish_date_time': get_date_time_object_from_string(search_response.get("snippet",{}).get('publishedAt',''))
    }

def get_video_thumbnails_from_result(search_response):
    '''
    Args: Takes Youtube Search Response
    Return: Formatted video thumbnails
    '''
    return [{
        'screen_size': screen_size,
        'url':  data.get('url','')
    } for screen_size, data in search_response.get('snippet',{}).get('thumbnails', {}).items()]


def search_and_add_youtube_videos_service():
    '''
    call the FetchAndStoreYouTubeSearchData view to fetch and store youtube search data
    '''
    from .views import FetchAndStoreYouTubeSearchData
    youtube_api_key = YoutubeAPIKeys.objects.filter(status=True).last()
    if youtube_api_key:
        published_after = datetime.now()
        get_and_store_yotube_search_data = FetchAndStoreYouTubeSearchData()
        params = {'query': 'News', 'max_search_results': 10, 'youtube_api_key': youtube_api_key, 'published_after': published_after}
        request = get_and_store_yotube_search_data.get_api_request(params)
        FetchAndStoreYouTubeSearchData.as_view()(request)