# Create your models here.
from django.db import models


class MyBlog(models.Model):
    title = models.CharField(max_length=100)
    artical = models.CharField(max_length=10000)
