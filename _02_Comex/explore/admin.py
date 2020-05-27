# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . models import Category
from . models import Partnership

from django.contrib import admin

admin.site.register(Category)
admin.site.register(Partnership)
# Register your models here.
