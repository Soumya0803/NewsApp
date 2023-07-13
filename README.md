# NewsApp
 
create .env in newsaggregator folder 

example 

NEWS_API_KEY = 'your_api_key'
DJANGO_SECRET_KEY = 'django_generate_secret'
DB_NAME = 'Newsapp'
DB_USER = 'postgres'
DB_PASSWORD = 'password'
DB_HOST = 'db'
DB_PORT = '5432'
CELERY_BROKER_REDIS_URL="redis://redis:6379"

run `docker compose up`
