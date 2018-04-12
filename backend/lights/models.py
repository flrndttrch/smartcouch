# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
# Create your models here.
from django.utils.timezone import now

class Type(models.Model):
    name = models.CharField(max_length=200)

class Lighting(models.Model):
    user = models.ForeignKey(User)
    # history = models.ForeignKey(LightingHistory, on_delete=models.CASCADE)
    type = models.ForeignKey(Type)
    brightness = models.FloatField(default=1.0, validators=[MaxValueValidator(1.0), MinValueValidator(0.0)])
    color_name = models.CharField(max_length=64, blank=True, null=True, unique=True)
    color_r = models.IntegerField(default=None, blank=True, null=True, validators=[MaxValueValidator(255), MinValueValidator(0)])
    color_g = models.IntegerField(default=None, blank=True, null=True, validators=[MaxValueValidator(255), MinValueValidator(0)])
    color_b = models.IntegerField(default=None, blank=True, null=True, validators=[MaxValueValidator(255), MinValueValidator(0)])
    creation_date = models.DateTimeField('date created', default=now)
    description = models.CharField(max_length=1024, blank=True, null=True)
    active = models.BooleanField(default=True)
