# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from flax_id.django.fields import FlaxId

# Create your models here.
class category(models.Model):
    id = FlaxId(primary_key=True)
    name = models.CharField(max_length=30)
    icon_url = models.CharField(max_length=256)

    def __str__(self):
        return self.name
