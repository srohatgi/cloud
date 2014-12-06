# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hunts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('commentId', models.CharField(max_length=37, serialize=False, primary_key=True)),
                ('comment', models.CharField(max_length=255)),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('updatedOn', models.DateTimeField(auto_now=True)),
                ('createdBy', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
                ('huntId', models.ForeignKey(related_name='+', to='hunts.Hunt')),
                ('updatedBy', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('createdOn',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('followId', models.CharField(max_length=37, serialize=False, primary_key=True)),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('updatedOn', models.DateTimeField(auto_now=True)),
                ('createdBy', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
                ('huntId', models.ForeignKey(related_name='+', to='hunts.Hunt')),
                ('updatedBy', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
                ('userId', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('createdOn',),
            },
            bases=(models.Model,),
        ),
    ]
