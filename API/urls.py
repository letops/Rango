from django.conf.urls import patterns, url
from rest_framework.views import ListOrCreateModelView, InstanceModelView
from Salus.resources import PasswordResource

my_model_list = ListOrCreateModelView.as_view(resource=PasswordResource)
my_model_instance = InstanceModelView.as_view(resource=PasswordResource)

urlpatterns = patterns('',
    url(r'^passwords/$', my_model_list, name='passwords_api_root'),
    url(r'^passwords/(?P<id>[0-9]+)/$', my_model_instance, name='passwords_api_instance'),
)