# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deliverable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headline', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headline', models.CharField(max_length=256)),
                ('deliverable', models.ForeignKey(to='omf.Deliverable')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.IntegerField(default=0)),
                ('order_for', models.CharField(max_length=256)),
                ('creator', models.CharField(max_length=256)),
                ('parent', models.ForeignKey(to='omf.Order', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.IntegerField(default=0)),
                ('headline', models.CharField(max_length=256)),
                ('notes', models.TextField(null=True)),
                ('order', models.ForeignKey(to='omf.Order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('report_datetime', models.DateTimeField(auto_now_add=True)),
                ('reporter', models.CharField(max_length=256)),
                ('status_note', models.TextField(null=True)),
                ('status_flag', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Promise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=256)),
                ('parameters', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ManyToManyField(to='omf.OrderStatus', null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='to',
            field=models.ForeignKey(to='epd.Endpoint'),
        ),
        migrations.AddField(
            model_name='deliverable',
            name='line_item',
            field=models.ForeignKey(to='omf.OrderLineItem'),
        ),
    ]
