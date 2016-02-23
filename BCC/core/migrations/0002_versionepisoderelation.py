# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VersionEpisodeRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('predicate', models.IntegerField(default=1)),
                ('episode', models.ForeignKey(to='core.Episode')),
                ('version', models.ForeignKey(to='core.Version')),
            ],
        ),
    ]
