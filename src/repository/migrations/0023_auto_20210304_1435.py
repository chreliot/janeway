# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-04 14:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0022_auto_20210303_1450'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={},
        ),
        migrations.AlterField(
            model_name='preprintauthor',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='repository.Author'),
        ),
    ]