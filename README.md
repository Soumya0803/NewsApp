# NewsApp
 ![NewsApp](doc_images/NewsApi.png)
create .env in newsaggregator folder 

example 
```
NEWS_API_KEY = 'your_api_key'
DJANGO_SECRET_KEY = 'django_generate_secret'
DB_NAME = 'Newsapp'
DB_USER = 'postgres'
DB_PASSWORD = 'password'
DB_HOST = 'db'
DB_PORT = '5432'
CELERY_BROKER_REDIS_URL="redis://redis:6379"
```
run `docker compose up`

News App displays the top headlines stored in the postgres DB for the past 7 days.
```
view: TopHeadlinesView
model: TopHeadlines
template: home.html
```

![NewsApp](doc_images/home.png)

Pagination is implemented for the top headlines  
 
![NewsApp](doc_images/home_pagination.png)

You can add and manage your periodic tasks from the Django Admin interface (Used django celery beat's  Database-backed Periodic Tasks) 
A daily schedule to retrieve news data (top headlines) every day is configured to run once a day at 12.am.utc for a period of one week (7 days). It is disabled after one week in the celery task file.

`task: populate_top_headlines_news_db`

![NewsApp](doc_images/admin.png) 
![NewsApp](doc_images/admin_tasks.png)

The hourly and daily news volume are plotted on graph using chart.js
```
view: volume_graphs
template: volume_graphs.html
 ```
Daily Volume

![NewsApp](doc_images/graph_daily.png)

Hourly Volume

![NewsApp](doc_images/graph_hourly.png)
