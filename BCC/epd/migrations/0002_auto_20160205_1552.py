# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epd', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deliverycontext',
            options={'verbose_name': 'Delivery Context', 'verbose_name_plural': 'Delivery Contexts'},
        ),
    ]
