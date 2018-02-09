# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Lighting(models.Model):
    name = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date created')
    description = models.CharField(max_length=1024)
    active = models.BooleanField(default=False)