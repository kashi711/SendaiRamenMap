# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_businesshour_wedclose2'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesshour',
            name='FriClose3',
            field=models.TimeField(default=b'0:00:00'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='businesshour',
            name='FriOpen3',
            field=models.TimeField(default=b'0:00:00'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='businesshour',
            name='MonClose3',
            field=models.TimeField(default=b'0:00:00'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='businesshour',
            name='MonOpen3',
            field=models.TimeField(default=b'0:00:00'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='businesshour',
            name='SatClose3',
            field=models.TimeField(default=b'0:00:00'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='businesshour',
            name='SatOpen3',
            field=models.TimeField(default=b'0:00:00'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='businesshour',
            name='SunClose3',
            field=models.TimeField(default=b'0:00:00'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='businesshour',
            name='SunOpen3',
            field=models.TimeField(default=b'0:00:00'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='businesshour',
            name='ThuClose3',
            field=models.TimeField(default=b'0:00:00'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='businesshour',
            name='ThuOpen3',
            field=models.TimeField(default=b'0:00:00'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='businesshour',
            name='TueClose3',
            field=models.TimeField(default=b'0:00:00'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='businesshour',
            name='TueOpen3',
            field=models.TimeField(default=b'0:00:00'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='businesshour',
            name='WedClose3',
            field=models.TimeField(default=b'0:00:00'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='businesshour',
            name='WedOpen3',
            field=models.TimeField(default=b'0:00:00'),
            preserve_default=True,
        ),
    ]
