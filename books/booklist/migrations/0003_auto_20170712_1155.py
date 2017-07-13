# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0002_booklist_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklist',
            name='author',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]
