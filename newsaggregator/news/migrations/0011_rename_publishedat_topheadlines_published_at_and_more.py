# Generated by Django 4.2.3 on 2023-07-12 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_alter_topheadlines_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topheadlines',
            old_name='publishedAt',
            new_name='published_at',
        ),
        migrations.RenameField(
            model_name='topheadlines',
            old_name='urlToImage',
            new_name='url_to_image',
        ),
    ]
