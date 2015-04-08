from django.conf.urls import patterns, url

urlpatterns = patterns('Salus.views',
   url(r'^password/$', view='GenericList', kwargs={'action': 'list_password'}, name='list_password'),
   url(r'^password/new$', view='object_push', kwargs={'action': 'add_password'}, name='add_password'),
   url(r'^password/(?P<id>\d+)$', view='object_push', kwargs={'action': 'change_password'}, name='change_password'),
   url(r'^password/(?P<id>\d+)/delete$', view='GenericList', kwargs={'action': 'list_password'}, name='delete_password'),

)