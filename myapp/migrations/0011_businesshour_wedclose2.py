# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_businesshour'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesshour',
            name='WedClose2',
            field=models.TimeField(default=b'0:00:00'),
            preserve_default=True,
        ),
    ]
