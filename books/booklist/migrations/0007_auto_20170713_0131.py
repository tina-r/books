# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0006_auto_20170713_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklist',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 12, 23, 31, 56, 722775, tzinfo=utc)),
        ),
    ]
