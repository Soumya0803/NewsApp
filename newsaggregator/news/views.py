from django.shortcuts import render
from decouple import config
from newsapi import NewsApiClient
from news.models import VolumeStatisticsDaily, TopHeadlines
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path
from django.db.models.functions import TruncHour
from django.db.models import Count

# Create your views here.

API_KEY = config('NEWS_API_KEY')

def top_headlines(request):
    newsapi = NewsApiClient(api_key=API_KEY)
    top_headlines = newsapi.get_top_headlines(language='en',country='us')
    # print(top_headlines)
    news_articles = top_headlines['articles']
    context = {
        'news_articles': news_articles
    }
    
    return render(request, 'home.html', context)



@staff_member_required
def volume_graphs(request):
    #daily
    daily_results = VolumeStatisticsDaily.objects.filter(created_at__gte=datetime.now()-timedelta(days=7)).values_list('total_results', 'created_at').order_by('created_at')
    localtz = ZoneInfo('localtime')
    label = []
    data = []
    for i in daily_results:
        data.append(i[0])
        #convert utc to local datetime to show correctly in graph
        # local_dt= i[1].astimezone(localtz) 
        # label.append(local_dt.strftime("%Y-%m-%d"))
        label.append(i[1].strftime("%Y-%m-%d")) #utc

    
    # hourly 
    # this is in utc for now
    last_index = len(daily_results) - 1
    last_date = daily_results[last_index][1].date()
    
    hourly_results = TopHeadlines.objects.filter(published_at__gte=last_date).annotate(hour=TruncHour('published_at')).values('hour').annotate(daily_results=Count('published_at')).order_by('hour')
    # print(hourly_results)
    hourly_label = []
    hourly_data = []
    # print(hourly_results)
    for i in hourly_results:
        hourly_label.append(i['hour'].strftime("%Y-%m-%d %H:%M"))
        hourly_data.append(i['daily_results'])

    context = {
     'label': label,
     'data' : data,
     'hourly_label': hourly_label,
     'hourly_data' : hourly_data
    }

    return render(request, 'volume_graph.html', context)

class CustomAdminSite(admin.AdminSite):
    def get_app_list(self, request, _=None):
        app_list = super().get_app_list(request)
        app_list += [
            {
                "name": "Custom Admin",
                "app_label": "custom_admin",
                "models": [
                    {
                        "name": "Statistics",
                        "object_name": "statistics",
                        "admin_url": "/admin/statistics",
                        "view_only": True,
                    }
                ],
            }
        ]
        return app_list

    def get_urls(self):
        urls = super().get_urls()
        urls += [
            path("statistics/", volume_graphs, name="admin-statistics"),
        ]
        return urls
    
