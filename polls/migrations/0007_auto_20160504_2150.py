# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 21:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20160501_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advisor',
            name='photo',
            field=models.ImageField(upload_to='/Users/chaoli/Workspace/python/advisor_selection_system/mysite/polls/static/faces/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='advisor',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Advisor'),
        ),
        migrations.AlterField(
            model_name='student',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
