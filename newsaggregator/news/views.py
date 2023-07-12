from django.shortcuts import render
from decouple import config
from newsapi import NewsApiClient
from news.models import VolumeStatisticsDaily
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path

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
    # daily_results = VolumeStatisticsDaily.objects.filter(created_at__gte=datetime.now()-timedelta(days=7)).values_list('total_results', flat=True).order_by('created_at')
    daily_results2 = VolumeStatisticsDaily.objects.filter(created_at__gte=datetime.now()-timedelta(days=7)).values_list('total_results', 'created_at').order_by('created_at')
    localtz = ZoneInfo('localtime')
    label = []
    data = []
    for i in daily_results2:
        data.append(i[0])
        #convert utc to local datetime to show correctly in graph
        local_dt= i[1].astimezone(localtz) 
        label.append(local_dt.day)
    context = {
    
    'label': label,
     'data' : data
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