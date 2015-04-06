from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Salus.views.dummy', name='home'),
    url(r'^login/$', view='Base.views.login', name='login'),
    url(r'^account$', include('Base.urls')),
    url(r'^salus/', include('Salus.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
