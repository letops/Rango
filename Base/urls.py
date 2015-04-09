from django.conf.urls import patterns, url

from Salus.models import Password

urlpatterns = patterns('Base.views',
   url(r'^users/$', view='GenericList', kwargs={'action': 'list_users'}, name='list_users'),
   url(r'^new/$', view='object_push', kwargs={'action': 'add_user'}, name='add_user'),
   url(r'^(?P<id>\d+)/$', view='object_push', kwargs={'action': 'change_user'}, name='change_user'),
   url(r'^(?P<id>\d+)/delete/$', view='GenericList', kwargs={'action': 'delete_user'}, name='delete_user'),
)
