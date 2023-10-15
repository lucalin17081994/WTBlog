from django.db import models

# Create your models here.
class BlogPost(models.Model):
    username = models.CharField(max_length=30)
    title=models.CharField(max_length=100)
    content = models.TextField()