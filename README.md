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
 ![NewsApp](doc_images/home.png)
 ![NewsApp](doc_images/home_pagination.png)
 ![NewsApp](doc_images/admin.png) 
 ![NewsApp](doc_images/admin_tasks.png)
 ![NewsApp](doc_images/graph_daily.png)
 ![NewsApp](doc_images/graph_hourly.png)
