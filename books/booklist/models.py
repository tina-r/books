# encoding: utf-8
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class BookList(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now)
    def __unicode__(self):
        return self.title
