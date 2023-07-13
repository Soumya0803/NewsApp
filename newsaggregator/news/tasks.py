from django_celery_beat.models import PeriodicTask
from celery import shared_task
from newsapi import NewsApiClient
from news.models import TopHeadlines, VolumeStatisticsDaily
from decouple import config
import requests
import math
import datetime

date = datetime.date.today()
disable_date = datetime.date(2023, 7, 20)

# disable after one week
if date > disable_date:
    periodic_task = PeriodicTask.objects.get(
        name="top_headlines-populate-news-db")
    periodic_task.enabled = False
    periodic_task.save()

API_KEY = config('NEWS_API_KEY')


@shared_task
def populate_top_headlines_news_db():
    CATEGORY_CHOICES = [
        'business',
        'entertainment',
        'general',
        'health',
        'science',
        'sports',
        'technology'
    ]
    daily_total_results = 0
    # newsapi = NewsApiClient(api_key=API_KEY)
    for category in CATEGORY_CHOICES:
        # top_headlines = newsapi.get_top_headlines(category=category)

        # initial_get
        pagesize = 20
        result = get_top_headlines_per_page(
            category, page=1, pagesize=pagesize)
        news_articles = result['articles']
        daily_total_results += result['totalResults']  # for all categories
        populate_db(news_articles, category)

        category_total_results = result['totalResults']
        total_pages = math.ceil(category_total_results/pagesize)

        # for page in range(2,total_pages+1):
        for page in range(2, 6):  # Developer account restricted to 100 results
            result = get_top_headlines_per_page(category, page, pagesize)
            print("result")
            print(result)
            if result:
                news_articles = result['articles']
                populate_db(news_articles, category)
            else:
                break
    # store daily total results
    daily_results = VolumeStatisticsDaily(total_results=daily_total_results)
    print('daily_results')
    print(daily_results)
    daily_results.save()


def get_top_headlines_per_page(category, page, pagesize):
    top_headlines = 'https://newsapi.org/v2/top-headlines'
    params = {
        'category': category,
        'apiKey': API_KEY,
        'pagesize': pagesize,
        'page': page
    }
    result = requests.get(top_headlines, params=params).json()
    return result


def populate_db(news_articles, category):
    for article in news_articles:
        article_data = TopHeadlines(
            source_id=article['source']['id'],
            source_name=article['source']['name'],
            author=article['author'],
            title=article['title'],
            description=article['description'],
            url=article['url'],
            url_to_image=article['urlToImage'],
            published_at=article['publishedAt'],
            content=article['content'],
            category=category
        )
        article_data.save()
