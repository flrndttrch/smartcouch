# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig



class LightsConfig(AppConfig):
    name = 'lights'

    def ready(self):
        import lights.services #noqa
