# encoding: utf-8
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class BookList(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.localtime(timezone.now()))
    author = models.CharField(max_length=255, default='')
    def __unicode__(self):
        return self.title

