# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_myreview_shop_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('evaluation', models.IntegerField()),
                ('pub_date', models.DateTimeField()),
                ('name', models.CharField(max_length=100)),
                ('shop', models.ForeignKey(to='myapp.Shop')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
