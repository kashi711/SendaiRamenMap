# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_evalinfo_int_eval'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='evaluation',
            field=models.DecimalField(default=0.0, max_digits=2, decimal_places=1),
            preserve_default=True,
        ),
    ]
