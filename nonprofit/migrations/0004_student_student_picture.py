# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-29 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nonprofit', '0003_auto_20170128_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_picture',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
