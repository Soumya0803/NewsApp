# Generated by Django 3.1.5 on 2023-07-10 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_id', models.CharField(max_length=100)),
                ('source_name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('url', models.URLField(blank=True, null=True)),
                ('urlToImage', models.URLField(blank=True, null=True)),
                ('publishedAt', models.DateTimeField()),
                ('content', models.TextField()),
                ('category', models.CharField(choices=[('business', 'Business'), ('entertainment', 'Entertainment'), ('general', 'General'), ('health', 'Health'), ('science', 'Science'), ('sports', 'Sports'), ('technology', 'Technology')], max_length=50)),
            ],
        ),
    ]
