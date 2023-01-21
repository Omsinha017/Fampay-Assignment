from rest_framework import serializers
from .models import Video, VideoThumnails

class VideoThumnailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoThumnails
        fields = "__all__"


class VideoSerializer(serializers.ModelSerializer):
    thumbnail = VideoThumnailsSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = "__all__"
    
