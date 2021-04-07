from django.db import models


class Food(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    ingredients = models.CharField(max_length=500, blank=False, default='')
    link = models.CharField(max_length=100, blank=False, default='')
    methods = models.CharField(max_length=500, blank=False, default='')
    thumbnail = models.CharField(max_length=100,blank=False, default='')

