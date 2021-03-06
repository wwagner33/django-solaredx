# -*- coding: utf-8 -*-

from tastypie.api import Api

from django.conf import settings
from django.conf.urls import patterns, url, include

from . import api_v1


v1_api = Api(api_name='v1')
v1_api.register(api_v1.UserResource())
v1_api.register(api_v1.CourseResource())

test_urls = patterns('solaredx.views',
    url(r'^login/$', 'auth_login', name='login'),    
    url(r'^ping/$', 'ping', name='ping'),
    url(r'^test/$', 'test', name='test'),
)

urlpatterns = patterns('',
    url(r'^', include(test_urls, namespace='solaredx', app_name='solaredx')),
    url(r'^api/', include(v1_api.urls)),
)

# Solução para utilização do Django Debug Toolbar
if settings.DEBUG:
    urlpatterns += patterns('solaredx.views', 
        url(r'^api/debug/', 'debug'),
    )