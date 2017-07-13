# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booklist',
            name='author',
            field=models.CharField(default=b'DEFAULT VALUE', max_length=255),
        ),
    ]
