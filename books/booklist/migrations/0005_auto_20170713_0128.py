# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0004_auto_20170713_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklist',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 12, 23, 28, 41, 477689, tzinfo=utc)),
        ),
    ]
