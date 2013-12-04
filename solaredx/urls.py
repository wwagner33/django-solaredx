# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import patterns, url, include

from tastypie.api import Api

from .api.resources.ping import PingResource
from .api.resources.users import UserResource, UserProfileResource
from .api.resources.courses import CourseResource


dev_api = Api(api_name='dev')
dev_api.register(PingResource())
dev_api.register(UserResource())
dev_api.register(CourseResource())


test_urls = patterns('solaredx.views',
    url(r'^ping/$', 'ping', name='ping'),
    url(r'^test/$', 'test', name='test'),
)

urlpatterns = patterns('',
    url(r'^api/', include(test_urls, namespace='solaredx', app_name='solaredx')),
    url(r'^api/', include(dev_api.urls)),
)

# Solução para utilização do Django Debug Toolbar
if settings.DEBUG:
    urlpatterns += patterns('solaredx.views', 
        url(r'^api/debug/', 'debug'),
    )