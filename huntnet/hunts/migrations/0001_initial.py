# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('createdBy', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
                ('ownerId', models.ForeignKey(related_name='hunts', to=settings.AUTH_USER_MODEL)),
                ('updatedBy', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
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
                ('createdBy', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updatedBy', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('createdOn',),
            },
            bases=(models.Model,),
        ),
    ]
