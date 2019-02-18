#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 14:22:03 2019

@author: starboard
"""

from django.conf.urls import url
from .views import HelloView

urlpatterns = [
    url(r'', HelloView.as_view(), name='index'),   
]