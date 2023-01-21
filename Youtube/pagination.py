from rest_framework.pagination import PageNumberPagination

class YoutubeSearchListPagination(PageNumberPagination):
    page_size = 10
