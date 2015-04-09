from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Base.views.home', name='home'),
    url(r'^signup/$', view='Base.views.signup', name='signup'),
    url(r'^login/$', view='Base.views.login', name='login'),
    url(r'^logout/$', view='Base.views.logout', name='logout'),
    url(r'^account/', include('Base.urls')),
    url(r'^salus/', include('Salus.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
