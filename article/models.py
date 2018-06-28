from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta(object):
        ordering = ['-date_time']


class Comment(models.Model):
    author = models.CharField(max_length=30)
    content = models.TextField(blank=True, null=True)
    date_time = models.DateTimeField(auto_now_add=True)
    article_id = models.ForeignKey(Article)
    def __str__(self):
        return self.author
    class Meta(object):
        ordering = ['date_time']


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    birth_date = models.DateField(blank=True)
