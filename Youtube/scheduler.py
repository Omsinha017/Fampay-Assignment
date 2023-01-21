from apscheduler.schedulers.background import BackgroundScheduler
from .utils import search_and_add_youtube_videos_service

def start():
    '''
    This will run the search_and_add_youtube_videos_service in background
    '''
    scheduler = BackgroundScheduler()
    scheduler.add_job(search_and_add_youtube_videos_service, 'interval', seconds=10) #run after every 10 seconds
    scheduler.start()