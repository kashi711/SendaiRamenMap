# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20150831_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='tags',
            field=models.CharField(default=b'', max_length=300),
            preserve_default=True,
        ),
    ]
