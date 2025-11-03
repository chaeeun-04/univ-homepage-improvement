from django.db import models

class MainContent(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')

class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()