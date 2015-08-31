# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_evalinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evalinfo',
            name='evaluation',
            field=models.DecimalField(default=0.0, max_digits=2, decimal_places=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evalinfo',
            name='five',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evalinfo',
            name='four',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evalinfo',
            name='one',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evalinfo',
            name='three',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evalinfo',
            name='total',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evalinfo',
            name='two',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
