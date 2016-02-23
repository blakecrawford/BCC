# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('vmid', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('order', models.PositiveIntegerField(default=1)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Customization',
                'verbose_name_plural': 'Customizations',
            },
        ),
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('vmid', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('order', models.PositiveIntegerField(default=1)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Customization Type',
                'verbose_name_plural': 'Customization Types',
            },
        ),
        migrations.CreateModel(
            name='BCP47Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'ordering': ('language', 'script', 'country'),
                'verbose_name': 'BCP-47 Language',
                'verbose_name_plural': 'BCP-47 Languages',
            },
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('vmid', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('short_name', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(null=True)),
                ('status', models.IntegerField(choices=[(0, b'Active'), (1, b'Inactive')])),
            ],
            options={
                'ordering': ('short_name',),
                'verbose_name': 'Channel',
                'verbose_name_plural': 'Channels',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('vmid', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('code2', models.CharField(max_length=2)),
                ('code3', models.CharField(max_length=3)),
                ('codeN', models.IntegerField()),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='CountrySubdivision',
            fields=[
                ('vmid', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('subcode', models.CharField(max_length=3)),
                ('country', models.ForeignKey(to='refdata.Country')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Country Subdivision',
                'verbose_name_plural': 'Country Subdivisions',
            },
        ),
        migrations.CreateModel(
            name='CustomizationPropertyRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('required', models.BooleanField(default=False)),
                ('order', models.PositiveIntegerField(default=1)),
                ('customization', models.ForeignKey(to='refdata.Activity')),
            ],
            options={
                'verbose_name': 'Customization-to-Object Property Relationship',
                'verbose_name_plural': 'Customization-to-Object Property Relationships',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('vmid', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='GenreAuthority',
            fields=[
                ('vmid', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('ref_link', models.URLField(null=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Genre Authority',
                'verbose_name_plural': 'Genre Authorities',
            },
        ),
        migrations.CreateModel(
            name='GenreType',
            fields=[
                ('vmid', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Genre Type',
                'verbose_name_plural': 'Genre Types',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('vmid', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('code2', models.CharField(max_length=2)),
                ('code3', models.CharField(max_length=3)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.CreateModel(
            name='ObjectProperty',
            fields=[
                ('vmid', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('object_type', models.CharField(max_length=256)),
                ('order', models.PositiveIntegerField(default=1)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Object Property',
                'verbose_name_plural': 'Object Properties',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('vmid', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1024)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Rating',
                'verbose_name_plural': 'Ratings',
            },
        ),
        migrations.CreateModel(
            name='RatingAuthority',
            fields=[
                ('vmid', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1024)),
                ('ref_link', models.URLField(null=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Rating Authority',
                'verbose_name_plural': 'Rating Authorities',
            },
        ),
        migrations.CreateModel(
            name='RatingContentDescriptor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descriptor', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('descriptor',),
                'verbose_name': 'Content Descriptor',
                'verbose_name_plural': 'Content Descriptors',
            },
        ),
        migrations.CreateModel(
            name='ScriptName',
            fields=[
                ('vmid', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=8)),
                ('number', models.IntegerField()),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Script Name',
                'verbose_name_plural': 'Script Names',
            },
        ),
        migrations.AddField(
            model_name='rating',
            name='authority',
            field=models.ForeignKey(to='refdata.RatingAuthority'),
        ),
        migrations.AddField(
            model_name='rating',
            name='descriptors',
            field=models.ManyToManyField(to='refdata.RatingContentDescriptor', blank=True),
        ),
        migrations.AddField(
            model_name='genre',
            name='authority',
            field=models.ForeignKey(to='refdata.GenreAuthority'),
        ),
        migrations.AddField(
            model_name='genre',
            name='parent',
            field=models.ForeignKey(blank=True, to='refdata.Genre', null=True),
        ),
        migrations.AddField(
            model_name='genre',
            name='type',
            field=models.ForeignKey(to='refdata.GenreType'),
        ),
        migrations.AddField(
            model_name='customizationpropertyrelation',
            name='object_property',
            field=models.ForeignKey(to='refdata.ObjectProperty'),
        ),
        migrations.AddField(
            model_name='bcp47language',
            name='country',
            field=models.ForeignKey(to='refdata.Country'),
        ),
        migrations.AddField(
            model_name='bcp47language',
            name='language',
            field=models.ForeignKey(to='refdata.Language'),
        ),
        migrations.AddField(
            model_name='bcp47language',
            name='script',
            field=models.ForeignKey(to='refdata.ScriptName'),
        ),
        migrations.AddField(
            model_name='activity',
            name='type',
            field=models.ForeignKey(to='refdata.ActivityType'),
        ),
    ]
