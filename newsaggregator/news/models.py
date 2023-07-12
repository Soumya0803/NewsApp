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
    urlToImage = models.URLField(max_length=1000, null=True)
    publishedAt = models.DateTimeField()
    content = models.TextField(null = True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)


