# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('omf', '0002_auto_20160203_1352'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deliverable',
            options={'verbose_name': 'Deliverable', 'verbose_name_plural': 'Deliverables'},
        ),
        migrations.AlterModelOptions(
            name='delivery',
            options={'verbose_name': 'Delivery', 'verbose_name_plural': 'Deliveries'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='orderlineitem',
            options={'verbose_name': 'Order Line Item', 'verbose_name_plural': 'Order Line Items'},
        ),
        migrations.AlterModelOptions(
            name='orderstatus',
            options={'verbose_name': 'Order Status', 'verbose_name_plural': 'order Statuses'},
        ),
        migrations.AlterModelOptions(
            name='promise',
            options={'verbose_name': 'Promise', 'verbose_name_plural': 'Promises'},
        ),
        migrations.AlterField(
            model_name='order',
            name='order_for',
            field=models.ForeignKey(related_name='order_from', to='epd.Endpoint'),
        ),
        migrations.AlterField(
            model_name='order',
            name='parent',
            field=models.ForeignKey(blank=True, to='omf.Order', null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='to',
            field=models.ForeignKey(related_name='order_to', to='epd.Endpoint'),
        ),
    ]
