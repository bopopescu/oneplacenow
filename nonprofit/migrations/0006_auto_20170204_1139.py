# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-04 11:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nonprofit', '0005_auto_20170131_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bridgeinstructorenroll',
            name='class_field',
            field=models.ForeignKey(db_column='class_id', on_delete=django.db.models.deletion.DO_NOTHING, to='nonprofit.Class'),
        ),
    ]
