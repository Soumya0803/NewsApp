import os
from celery import Celery
from decouple import config
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsaggregator.settings')

app = Celery('newsaggregator')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'top_headlines-populate-news-db': {
        'task': 'populate_top_headlines_news_db',
        'schedule': crontab(minute=0, hour=0)

,
    }, 
}
