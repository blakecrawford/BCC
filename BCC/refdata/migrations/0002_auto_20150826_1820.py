# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('refdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityPropertyRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('required', models.BooleanField(default=False)),
                ('order', models.PositiveIntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Activity-to-Object Property Relationship',
                'verbose_name_plural': 'Activity-to-Object Property Relationships',
            },
        ),
        migrations.RemoveField(
            model_name='customizationpropertyrelation',
            name='customization',
        ),
        migrations.RemoveField(
            model_name='customizationpropertyrelation',
            name='object_property',
        ),
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ('name',), 'verbose_name': 'Activity', 'verbose_name_plural': 'Activities'},
        ),
        migrations.AlterModelOptions(
            name='activitytype',
            options={'ordering': ('name',), 'verbose_name': 'Activity Type', 'verbose_name_plural': 'Activity Types'},
        ),
        migrations.DeleteModel(
            name='CustomizationPropertyRelation',
        ),
        migrations.AddField(
            model_name='activitypropertyrelation',
            name='activity',
            field=models.ForeignKey(to='refdata.Activity'),
        ),
        migrations.AddField(
            model_name='activitypropertyrelation',
            name='object_property',
            field=models.ForeignKey(to='refdata.ObjectProperty'),
        ),
    ]
