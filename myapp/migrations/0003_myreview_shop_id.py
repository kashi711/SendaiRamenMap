# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_myreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='myreview',
            name='shop_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
