from django.db import models

CATEGORY_CHOICES = [
    ('business','Business'),
    ('entertainment','Entertainment'),
    ('general','General'),
    ('health','Health'),
    ('science','Science'),
    ('sports','Sports'),
    ('technology','Technology')
]

class TopHeadlines(models.Model):
    source_id = models.CharField(max_length=100, null= True)
    source_name =  models.CharField(max_length=100)
    author =  models.CharField(max_length=100, null= True)
    title =  models.CharField(max_length=1000)
    description =  models.CharField(max_length=1000,null=True)
    url = models.URLField(max_length=10000, null=True)
    url_to_image = models.URLField(max_length=1000, null=True)
    published_at = models.DateTimeField()
    content = models.TextField(null = True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)


class VolumeStatisticsDaily(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    total_results = models.IntegerField()