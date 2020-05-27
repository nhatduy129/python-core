# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-27 17:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import flax_id.django.fields


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0002_auto_20200527_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partnership',
            fields=[
                ('id', flax_id.django.fields.FlaxId(editable=False, max_length=16, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('date', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(max_length=512)),
                ('photo_thumb_url', models.URLField(max_length=512)),
                ('photo_url', models.URLField(max_length=512)),
                ('short_description', models.CharField(blank=True, max_length=512, null=True)),
                ('description', models.TextField(blank=True, max_length=1024, null=True)),
                ('link', models.URLField(blank=True, max_length=512, null=True)),
                ('link_title', models.CharField(max_length=50)),
                ('is_highlights', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='icon_url',
            field=models.URLField(max_length=512),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=256),
        ),
        migrations.AddField(
            model_name='partnership',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partnership', to='explore.Category'),
        ),
    ]