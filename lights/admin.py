# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from lights.models import Lighting, LightingHistory

admin.site.register(LightingHistory)
admin.site.register(Lighting)