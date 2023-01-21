from django.apps import AppConfig

class YoutubeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Youtube'

    def ready(self):
        from Youtube import scheduler
        scheduler.start()