# NewsApp
 ![NewsApp](doc_images/NewsApi.png)
create .env in newsaggregator folder 

## Installation Instructions

- Docker
Download and setup docker and docker compose for your machine 
https://docs.docker.com/engine/install/

- Go to Newsaggregator directory
`cd newsaggregator`

- Create .env file
`touch .env`


- Put the following content
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
	Note: If you are using docker compose, just change NEWS_API_KEY and DJANGO_SECRET_KEY

- run `docker compose up`
	Note1: Docker will automatically create DB and run Scheme migrations
	Note2: When running for the first time
	- Admin User will be created with credentials Username: `admin`, Password: `adminpassword`
	- DB will be automatically populated from NewsAPI
  

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
