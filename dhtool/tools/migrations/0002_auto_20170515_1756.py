# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mappingtools',
            name='cost_non_penn',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='mappingtools',
            name='cost_penn',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='mappingtools',
            name='data_input_format',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='mappingtools',
            name='data_output_format',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='mappingtools',
            name='notes',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='mappingtools',
            name='other_research_guides',
            field=models.URLField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='mappingtools',
            name='penn_research_guides',
            field=models.URLField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='mappingtools',
            name='software_link',
            field=models.URLField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='mappingtools',
            name='software_name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]