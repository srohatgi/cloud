__author__ = 'sumeetrohatgi'

from django.conf.urls import url
from hunts import views

urlpatterns = [
    url(r'^hunts/$', views.hunt_list),
    url(r'^hunts/(?P<pk>[a-z0-9\-]+)/$', views.hunt_detail),
]