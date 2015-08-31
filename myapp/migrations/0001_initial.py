# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('tell', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('opening', models.CharField(max_length=100)),
                ('closed', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=100)),
                ('lat', models.DecimalField(max_digits=9, decimal_places=6)),
                ('lng', models.DecimalField(max_digits=9, decimal_places=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
