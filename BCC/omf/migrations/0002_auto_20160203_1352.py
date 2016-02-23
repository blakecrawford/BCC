# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('omf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ManyToManyField(to='omf.OrderStatus'),
        ),
    ]
