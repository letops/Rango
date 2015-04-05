#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.utils import ListOrCreateModelView, InstanceModelView
from Salus.resources import PasswordResource
import Salus

my_model_list = ListOrCreateModelView.as_view(resource=PasswordResource)
my_model_instance = InstanceModelView.as_view(resource=PasswordResource)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Salus.views.dummy', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^passwords/', include('Salus.urls')),
    url(r'^api/1.0/', include('API.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
