__author__ = 'barisariburnu'

from django.conf.urls import patterns, url
from member import views
import django.contrib.auth

urlpatterns = patterns('',
                        url(r'^new_member/$', 'member.views.new_member'),
                        url(r'^member_profile/$', 'member.views.member_profile'),
                        )