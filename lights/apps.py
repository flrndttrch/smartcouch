# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class LightsConfig(AppConfig):
    name = 'lights'

    # def ready(self):
    #     # This line dispatches signal to Tastypie to create APIKey
    #     signals.post_save.connect(create_api_key, sender=User)
