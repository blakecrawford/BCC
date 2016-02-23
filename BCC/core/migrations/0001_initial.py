# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('refdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClipEpisodeRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('predicate', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CustomizationSpecification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('property_target', models.CharField(max_length=1024)),
                ('customization', models.ForeignKey(to='refdata.Activity')),
                ('object_property', models.ForeignKey(to='refdata.ObjectProperty')),
            ],
        ),
        migrations.CreateModel(
            name='Endeavor',
            fields=[
                ('vmid', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('description', models.TextField(max_length=1024, null=True)),
            ],
            options={
                'ordering': ('vmid',),
                'verbose_name': 'Endeavor',
                'verbose_name_plural': 'Endeavors',
            },
        ),
        migrations.CreateModel(
            name='EpisodeSeasonRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('predicate', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ModuleEpisodeRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('predicate', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MovieFranchiseRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('predicate', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SeasonSeriesRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('predicate', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SeriesFranchiseRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('predicate', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SpecialSeriesRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('predicate', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('vmid', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('title_text', models.CharField(max_length=1056)),
            ],
            options={
                'ordering': ('title_text',),
                'verbose_name': 'Title',
                'verbose_name_plural': 'Titles',
            },
        ),
        migrations.CreateModel(
            name='TitleType',
            fields=[
                ('vmid', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('length_restriction', models.IntegerField(null=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Title Type',
                'verbose_name_plural': 'Title Types',
            },
        ),
        migrations.CreateModel(
            name='ContentContainer',
            fields=[
                ('endeavor_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.Endeavor')),
                ('default_title', models.CharField(default=b'title', max_length=255)),
                ('cctype', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('cctype', 'vmid'),
                'verbose_name': 'Content Container',
                'verbose_name_plural': 'Content Containers',
            },
            bases=('core.endeavor',),
        ),
        migrations.CreateModel(
            name='ContentItem',
            fields=[
                ('endeavor_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.Endeavor')),
                ('citype', models.IntegerField(default=0)),
                ('default_title', models.CharField(default=b'title', max_length=255)),
            ],
            options={
                'ordering': ('citype', 'vmid'),
                'verbose_name': 'Content Item',
                'verbose_name_plural': 'Content Item',
            },
            bases=('core.endeavor',),
        ),
        migrations.AddField(
            model_name='title',
            name='endeavor',
            field=models.ForeignKey(to='core.Endeavor'),
        ),
        migrations.AddField(
            model_name='title',
            name='language',
            field=models.ForeignKey(to='refdata.BCP47Language', null=True),
        ),
        migrations.AddField(
            model_name='title',
            name='title_type',
            field=models.ForeignKey(to='core.TitleType'),
        ),
        migrations.AddField(
            model_name='endeavor',
            name='country_of_origin',
            field=models.ForeignKey(to='refdata.Country', null=True),
        ),
        migrations.AddField(
            model_name='endeavor',
            name='reference_channel',
            field=models.ForeignKey(to='refdata.Channel', null=True),
        ),
        migrations.CreateModel(
            name='Clip',
            fields=[
                ('contentitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.ContentItem')),
            ],
            options={
                'verbose_name': 'Clip',
                'verbose_name_plural': 'Clip',
            },
            bases=('core.contentitem',),
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('contentitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.ContentItem')),
                ('typical_length', models.CharField(max_length=12, null=True)),
                ('production_number', models.CharField(max_length=10, null=True)),
            ],
            options={
                'verbose_name': 'Episode',
                'verbose_name_plural': 'Episode',
            },
            bases=('core.contentitem',),
        ),
        migrations.CreateModel(
            name='Franchise',
            fields=[
                ('contentcontainer_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.ContentContainer')),
            ],
            options={
                'verbose_name': 'Franchise',
                'verbose_name_plural': 'Franchises',
            },
            bases=('core.contentcontainer',),
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('contentitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.ContentItem')),
                ('typical_length', models.CharField(max_length=12, null=True)),
            ],
            options={
                'verbose_name': 'Module',
                'verbose_name_plural': 'Module',
            },
            bases=('core.contentitem',),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('contentitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.ContentItem')),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movie',
            },
            bases=('core.contentitem',),
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('contentcontainer_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.ContentContainer')),
                ('number', models.IntegerField(null=True)),
                ('sequence', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name': 'Season',
                'verbose_name_plural': 'Season',
            },
            bases=('core.contentcontainer',),
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('contentcontainer_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.ContentContainer')),
                ('typical_length', models.CharField(max_length=12, null=True)),
                ('reference_language', models.ForeignKey(to='refdata.BCP47Language', null=True)),
            ],
            options={
                'verbose_name': 'Series',
                'verbose_name_plural': 'Series',
            },
            bases=('core.contentcontainer',),
        ),
        migrations.CreateModel(
            name='Special',
            fields=[
                ('contentitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.ContentItem')),
            ],
            options={
                'verbose_name': 'Special',
                'verbose_name_plural': 'Special',
            },
            bases=('core.contentitem',),
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('contentitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.ContentItem')),
                ('label', models.CharField(default=b'label', max_length=1024)),
            ],
            options={
                'ordering': ('label',),
                'verbose_name': 'Version',
                'verbose_name_plural': 'Versions',
            },
            bases=('core.contentitem',),
        ),
        migrations.AddField(
            model_name='specialseriesrelation',
            name='series',
            field=models.ForeignKey(to='core.Series'),
        ),
        migrations.AddField(
            model_name='specialseriesrelation',
            name='special',
            field=models.ForeignKey(to='core.Special'),
        ),
        migrations.AddField(
            model_name='seriesfranchiserelation',
            name='franchise',
            field=models.ForeignKey(to='core.Franchise'),
        ),
        migrations.AddField(
            model_name='seriesfranchiserelation',
            name='series',
            field=models.ForeignKey(to='core.Series'),
        ),
        migrations.AddField(
            model_name='seasonseriesrelation',
            name='season',
            field=models.ForeignKey(to='core.Season'),
        ),
        migrations.AddField(
            model_name='seasonseriesrelation',
            name='series',
            field=models.ForeignKey(to='core.Series'),
        ),
        migrations.AddField(
            model_name='moviefranchiserelation',
            name='franchise',
            field=models.ForeignKey(to='core.Franchise'),
        ),
        migrations.AddField(
            model_name='moviefranchiserelation',
            name='movie',
            field=models.ForeignKey(to='core.Movie'),
        ),
        migrations.AddField(
            model_name='moduleepisoderelation',
            name='episode',
            field=models.ForeignKey(to='core.Episode'),
        ),
        migrations.AddField(
            model_name='moduleepisoderelation',
            name='module',
            field=models.ForeignKey(to='core.Module'),
        ),
        migrations.AddField(
            model_name='episodeseasonrelation',
            name='episode',
            field=models.ForeignKey(to='core.Episode'),
        ),
        migrations.AddField(
            model_name='episodeseasonrelation',
            name='season',
            field=models.ForeignKey(to='core.Season'),
        ),
        migrations.AddField(
            model_name='customizationspecification',
            name='for_version',
            field=models.ForeignKey(blank=True, to='core.Version', null=True),
        ),
        migrations.AddField(
            model_name='clipepisoderelation',
            name='clip',
            field=models.ForeignKey(to='core.Clip'),
        ),
        migrations.AddField(
            model_name='clipepisoderelation',
            name='episode',
            field=models.ForeignKey(to='core.Episode'),
        ),
    ]
