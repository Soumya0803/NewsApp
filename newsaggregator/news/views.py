from django.shortcuts import render
import requests
from decouple import config
from newsapi import NewsApiClient

# Create your views here.

API_KEY = config('NEWS_API_KEY')

COUNTRY = 'us'

def top_headlines(request):
    newsapi = NewsApiClient(api_key=API_KEY)
    top_headlines = newsapi.get_top_headlines(language='en',country='us')
    print(top_headlines)
    news_articles = top_headlines['articles']
    
    context = {
        'news_articles': news_articles
    }

    return render(request, 'home.html', context)
