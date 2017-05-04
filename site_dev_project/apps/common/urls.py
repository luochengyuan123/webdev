#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017/04/28
@author: oliver
common模块的url配置。
"""

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^search/', search, name='search'),
    url(r'^careercourse/$', careercourse, name='careercourse'),
    url(r'^careercourse/course/$', detailcourse, name='course'),
    url(r'^teacher/$', teacher, name='teacher'),
    url(r'^search/$', search, name='search'),
    url(r'^login/$', login, name='login'),

    #个人中心

    url(r'^information/$', myinformation, name='information'),
    url(r'^information/information/$', myinformation, name='information'),
    url(r'^information/course/$', mycourse, name='course'),
    url(r'^information/collect/$', mycollect, name='collect'),
    url(r'^information/certificate/$', mycertificate, name='certificate'),
    url(r'^information/message/$', mymessage, name='message'),



    url(r'^logout$', do_logout, name='logout'),
    # url(r'^reg', do_reg, name='reg'),
    # url(r'^login', do_login, name='login'),


]
