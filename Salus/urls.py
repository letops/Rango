from django.conf.urls import patterns, url

urlpatterns = patterns('Salus.views',
   url(r'^password/$', view='GenericList', kwargs={'action': 'list_passwords'}, name='list_passwords'),
   url(r'^password/new$', view='GenericList', kwargs={'action': 'list_passwords'}, name='add_password'),
   url(r'^password/(?P<id>\d+)$', view='GenericList', kwargs={'action': 'list_passwords'}, name='change_password'),
   url(r'^password/(?P<id>\d+)/delete$', view='GenericList', kwargs={'action': 'list_passwords'}, name='delete_password'),

)