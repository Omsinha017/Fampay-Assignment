from django.db import models

class BasicDetails(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Video(BasicDetails):
    title = models.CharField(max_length=255)
    description = models.TextField()
    publish_date_time = models.DateTimeField(auto_now=False)
    video_id = models.CharField(max_length=255, unique=True)
    channel_id = models.CharField(max_length=255)
    channel_name = models.CharField(max_length=255)

    class Meta:
        ordering = ['-publish_date_time']

    def __str__(self):
        return self.title

class VideoThumnails(BasicDetails):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="thumbnail")
    screen_size = models.CharField(max_length=20)
    url = models.TextField()

    def __str__(self):
        return self.video.title

class YoutubeAPIKeys(BasicDetails):
    key = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.key

