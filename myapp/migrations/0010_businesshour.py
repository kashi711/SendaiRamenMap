# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_shop_int_eval'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessHour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('MonOpen1', models.TimeField(default=b'0:00:00')),
                ('MonClose1', models.TimeField(default=b'0:00:00')),
                ('MonOpen2', models.TimeField(default=b'0:00:00')),
                ('MonClose2', models.TimeField(default=b'0:00:00')),
                ('TueOpen1', models.TimeField(default=b'0:00:00')),
                ('TueClose1', models.TimeField(default=b'0:00:00')),
                ('TueOpen2', models.TimeField(default=b'0:00:00')),
                ('TueClose2', models.TimeField(default=b'0:00:00')),
                ('WedOpen1', models.TimeField(default=b'0:00:00')),
                ('WedOpen2', models.TimeField(default=b'0:00:00')),
                ('WedClose1', models.TimeField(default=b'0:00:00')),
                ('ThuOpen1', models.TimeField(default=b'0:00:00')),
                ('ThuClose1', models.TimeField(default=b'0:00:00')),
                ('ThuOpen2', models.TimeField(default=b'0:00:00')),
                ('ThuClose2', models.TimeField(default=b'0:00:00')),
                ('FriOpen1', models.TimeField(default=b'0:00:00')),
                ('FriClose1', models.TimeField(default=b'0:00:00')),
                ('FriOpen2', models.TimeField(default=b'0:00:00')),
                ('FriClose2', models.TimeField(default=b'0:00:00')),
                ('SatOpen1', models.TimeField(default=b'0:00:00')),
                ('SatClose1', models.TimeField(default=b'0:00:00')),
                ('SatOpen2', models.TimeField(default=b'0:00:00')),
                ('SatClose2', models.TimeField(default=b'0:00:00')),
                ('SunOpen1', models.TimeField(default=b'0:00:00')),
                ('SunClose1', models.TimeField(default=b'0:00:00')),
                ('SunOpen2', models.TimeField(default=b'0:00:00')),
                ('SunClose2', models.TimeField(default=b'0:00:00')),
                ('shop', models.ForeignKey(to='myapp.Shop')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
