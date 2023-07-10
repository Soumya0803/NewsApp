from django.urls import path
from .views import top_headlines
urlpatterns = [
    path('', top_headlines, name='home'),
]
