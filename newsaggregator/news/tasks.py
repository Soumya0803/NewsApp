from celery import shared_task
from newsapi import NewsApiClient
from news.models import News

@shared_task
def populate_top_headlines_news_db():

    API_KEY = config('NEWS_API_KEY')
    CATEGORY_CHOICES = [
    'business',
    'entertainment',
    'general',
    'health',
    'science',
    'sports',
    'technology'
    ]
    
    newsapi = NewsApiClient(api_key=API_KEY)
    for category in CATEGORY_CHOICES:
        print (category)
        top_headlines = newsapi.get_top_headlines(category=category)
        news_articles = top_headlines['articles']

        for article in news_articles[5:7]:
            article_data = News(
                source_id = article['source']['id'],
                source_name = article['source']['name'],
                author = article['author'],
                title =  article['title'],
                description =  article['description'],
                url = article['url'],
                urlToImage = article['urlToImage'],
                publishedAt = article['publishedAt'],
                content = article['content'],
                category = category
            )
            article_data.save()
