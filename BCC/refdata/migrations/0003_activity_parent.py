# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('refdata', '0002_auto_20150826_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='parent',
            field=models.ForeignKey(related_name='subactivities', blank=True, to='refdata.Activity', null=True),
        ),
    ]
