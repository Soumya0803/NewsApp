from django.urls import path
from .views import TopHeadlinesView
urlpatterns = [
    path('', TopHeadlinesView.as_view(), name='top_headlines'),
]
