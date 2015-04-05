#-*- coding:utf-8 -*-
from django.db import models


# Create your models here.
class Password(models.Model):
    """
    Represents a username and password together with several other fields
    """
    title = models.CharField(max_length=200)
    username = models.CharField(max_length=200, blank=True)
    password = models.CharField(max_length=200)
    url = models.URLField(max_length=500, blank=True, verbose_name='Site URL')
    notes = models.TextField(
        max_length=500,
        blank=True,
        help_text='Any extra notes')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    def __unicode__(self):
        return self.title