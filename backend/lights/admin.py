# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from lights.models import Lighting, Type, Day, Timer

admin.site.register(Lighting)
admin.site.register(Type)
admin.site.register(Day)
admin.site.register(Timer)
