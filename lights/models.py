# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from django.utils.timezone import now


class Lighting(models.Model):
    #history = models.ForeignKey(LightingHistory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date created', default=now)
    description = models.CharField(max_length=1024)
    active = models.BooleanField(default=True)


class LightingHistory(models.Model):
    lighting = models.ForeignKey(Lighting, on_delete=models.CASCADE)
    user = models.ForeignKey(User)
    activation_date = models.DateTimeField('date activated', default=now)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super(LightingHistory, self).save(force_insert, force_update, using, update_fields)

        Lighting.objects.all().exclude(pk=self.pk).update(active=False)



