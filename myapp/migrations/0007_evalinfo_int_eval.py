# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20150223_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='evalinfo',
            name='int_eval',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
