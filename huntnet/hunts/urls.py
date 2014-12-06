__author__ = 'sumeetrohatgi'

from django.conf.urls import url
from hunts import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^hunts/$', views.HuntList.as_view()),
    url(r'^hunts/(?P<pk>[a-z0-9\-]+)/$', views.HuntDetail.as_view()),
    url(r'^businesses/$', views.BusinessList.as_view()),
    url(r'^businesses/(?P<pk>[a-z0-9\-]+)/$', views.BusinessDetail.as_view()),
    url(r'^follows/$', views.FollowList.as_view()),
    url(r'^follows/(?P<pk>[a-z0-9\-]+)/$', views.FollowDetail.as_view()),
    url(r'^comments/$', views.CommentList.as_view()),
    url(r'^comments/(?P<pk>[a-z0-9\-]+)/$', views.CommentDetail.as_view()),
]

# understand requested format by url endpoint
urlpatterns = format_suffix_patterns(urlpatterns)