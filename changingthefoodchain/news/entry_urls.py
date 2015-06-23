from django.conf.urls import patterns, url

from news.views import EntryDetail, EntryList


urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)$', EntryDetail.as_view()),
    url(r'', EntryList.as_view()),
)
