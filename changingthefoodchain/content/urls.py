from django.conf.urls import patterns, url

from .views import PhotoList, VideoList


urlpatterns = patterns('',

    url(r'^photos/$', PhotoList.as_view()),

    url(r'^videos/$', VideoList.as_view()),

)
