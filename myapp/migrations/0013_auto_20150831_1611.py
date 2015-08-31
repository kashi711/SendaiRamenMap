# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20150303_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='cluster',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shop',
            name='tags',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
    ]
