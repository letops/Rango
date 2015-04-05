#-*- coding:utf-8 -*-
from django.conf.urls import patterns, url

from Salus.models import Password

urlpatterns = patterns('Salus.views',
    url(r'^$', 'password_list', name='password_list'),
)