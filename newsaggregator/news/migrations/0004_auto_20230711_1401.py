# Generated by Django 3.1.5 on 2023-07-11 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20230711_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]