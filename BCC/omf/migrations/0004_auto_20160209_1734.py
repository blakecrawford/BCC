# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('omf', '0003_auto_20160205_1552'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderstatus',
            options={'verbose_name': 'Order Status', 'verbose_name_plural': 'Order Statuses'},
        ),
    ]
