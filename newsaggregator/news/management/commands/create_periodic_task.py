# create_periodic_task.py

from django.core.management.base import BaseCommand
from django_celery_beat.models import CrontabSchedule, PeriodicTask
from celery import current_app
from news.tasks import populate_top_headlines_news_db


class Command(BaseCommand):
    help = 'Create Celery Beat periodic task if not already created'

    def handle(self, *args, **options):
        schedule, _ = CrontabSchedule.objects.get_or_create(
            minute='0',
            hour='0',
            day_of_week='*',
            day_of_month='*',
            month_of_year='*',
        )

        task, _ = PeriodicTask.objects.get_or_create(
            crontab=schedule,
            name='top_headlines-populate-news-db',
            task='news.tasks.populate_top_headlines_news_db',
        )

        if _:
            task = PeriodicTask.objects.get(
                name='top_headlines-populate-news-db')

            # Get the task function using the task's `task` attribute
            task_function = current_app.tasks[task.task]

            # Invoke the task asynchronously using `apply_async()`
            result = task_function.apply_async()

            self.stdout.write(self.style.SUCCESS(
                'Periodic task created successfully'))
        else:
            self.stdout.write(self.style.SUCCESS(
                'Periodic task already exists'))
