# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('omf', '0004_auto_20160209_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(to='omf.OrderStatus', null=True),
        ),
    ]
