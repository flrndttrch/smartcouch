# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from lights.models import Lighting, Type

admin.site.register(Lighting)
admin.site.register(Type)