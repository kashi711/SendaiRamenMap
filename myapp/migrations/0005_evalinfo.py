# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='evalInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total', models.IntegerField()),
                ('evaluation', models.DecimalField(max_digits=2, decimal_places=1)),
                ('one', models.IntegerField()),
                ('two', models.IntegerField()),
                ('three', models.IntegerField()),
                ('four', models.IntegerField()),
                ('five', models.IntegerField()),
                ('shop', models.ForeignKey(to='myapp.Shop')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
