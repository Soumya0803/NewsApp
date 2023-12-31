# Generated by Django 4.2.3 on 2023-07-12 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_rename_news_topheadlines'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topheadlines',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='topheadlines',
            name='url',
            field=models.URLField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='topheadlines',
            name='urlToImage',
            field=models.URLField(max_length=500, null=True),
        ),
    ]
