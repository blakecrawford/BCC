# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryContext',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryProcess',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bpmn', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Delivery Process',
                'verbose_name_plural': 'Delivery Processes',
            },
        ),
        migrations.CreateModel(
            name='Endpoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Endpoint',
                'verbose_name_plural': 'Endpoints',
            },
        ),
        migrations.CreateModel(
            name='EntityType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Entity Type',
                'verbose_name_plural': 'Entity Types',
            },
        ),
        migrations.CreateModel(
            name='MetadataSchema',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('schema', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Metadata Schema',
                'verbose_name_plural': 'Metadata Schemas',
            },
        ),
        migrations.CreateModel(
            name='PackageStructure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('structure_template', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Package Structure',
                'verbose_name_plural': 'Package Structures',
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Platform',
                'verbose_name_plural': 'Platforms',
            },
        ),
        migrations.CreateModel(
            name='StaticImageRequirements',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Static Image Requirement',
                'verbose_name_plural': 'Static Image Requirements',
            },
        ),
        migrations.CreateModel(
            name='TechnicalVideoRequirements',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Technical Video Requirement',
                'verbose_name_plural': 'Technical Video Requirements',
            },
        ),
        migrations.AddField(
            model_name='deliverycontext',
            name='delivery_process',
            field=models.ForeignKey(to='epd.DeliveryProcess'),
        ),
        migrations.AddField(
            model_name='deliverycontext',
            name='endpoint',
            field=models.ForeignKey(to='epd.Endpoint'),
        ),
        migrations.AddField(
            model_name='deliverycontext',
            name='entity_type',
            field=models.ForeignKey(to='epd.EntityType'),
        ),
        migrations.AddField(
            model_name='deliverycontext',
            name='image_requirements',
            field=models.ForeignKey(to='epd.StaticImageRequirements'),
        ),
        migrations.AddField(
            model_name='deliverycontext',
            name='metadata_schema',
            field=models.ForeignKey(to='epd.MetadataSchema'),
        ),
        migrations.AddField(
            model_name='deliverycontext',
            name='package_structure',
            field=models.ForeignKey(to='epd.PackageStructure'),
        ),
        migrations.AddField(
            model_name='deliverycontext',
            name='platform',
            field=models.ForeignKey(to='epd.Platform'),
        ),
        migrations.AddField(
            model_name='deliverycontext',
            name='technical_requirements',
            field=models.ForeignKey(to='epd.TechnicalVideoRequirements'),
        ),
    ]
