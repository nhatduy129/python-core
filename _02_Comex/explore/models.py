# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from flax_id.django.fields import FlaxId

# Create your models here.
class Category(models.Model):
    id = FlaxId(primary_key=True)
    name = models.CharField(max_length=256)
    icon_url = models.URLField(max_length=512)

    def __str__(self):
        return self.name

class Partnership(models.Model):
    id = FlaxId(primary_key=True)
    category = models.ForeignKey('explore.Category',
                                 related_name='partnership',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=512)
    photo_thumb_url = models.URLField(max_length=512)
    photo_url = models.URLField(max_length=512)
    short_description = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(max_length=1024, blank=True, null=True)
    link = models.URLField(max_length=512, blank=True, null=True)
    link_title = models.CharField(max_length=50, blank=True, null=True)
    is_highlights = models.BooleanField(default=False)

    def __str__(self):
        return self.name