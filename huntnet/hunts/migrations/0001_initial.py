# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('businessId', models.CharField(max_length=37, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=32)),
                ('addressLine1', models.CharField(max_length=255)),
                ('addressLine2', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
                ('zip', models.CharField(max_length=32)),
                ('contact', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255)),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('updatedOn', models.DateTimeField(auto_now=True)),
                ('createdBy', models.ForeignKey(related_name='+', to='hunts.Business')),
            ],
            options={
                'ordering': ('createdOn',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hunt',
            fields=[
                ('huntId', models.CharField(max_length=37, serialize=False, primary_key=True)),
                ('category', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('price', models.DecimalField(default=0, max_digits=12, decimal_places=2)),
                ('currency', models.CharField(default=b'USD', max_length=3)),
                ('minimum', models.IntegerField()),
                ('committed', models.IntegerField()),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('updatedOn', models.DateTimeField(auto_now=True)),
                ('businessId', models.ForeignKey(to='hunts.Business')),
            ],
            options={
                'ordering': ('createdOn',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.CharField(max_length=37, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('login', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('updatedOn', models.DateTimeField(auto_now=True)),
                ('createdBy', models.ForeignKey(related_name='+', to='hunts.User')),
                ('updatedBy', models.ForeignKey(related_name='+', to='hunts.User')),
            ],
            options={
                'ordering': ('createdOn',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='hunt',
            name='createdBy',
            field=models.ForeignKey(related_name='+', to='hunts.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hunt',
            name='updatedBy',
            field=models.ForeignKey(related_name='+', to='hunts.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='business',
            name='ownerId',
            field=models.ForeignKey(to='hunts.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='business',
            name='updatedBy',
            field=models.ForeignKey(related_name='+', to='hunts.Business'),
            preserve_default=True,
        ),
    ]
