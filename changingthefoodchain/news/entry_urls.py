from django.conf.urls import patterns, url

from news.views import EntryDetail, EntryGeoJSONList, EntryList


urlpatterns = patterns('',
    url(r'^geojson/$', EntryGeoJSONList.as_view()),
    url(r'^(?P<pk>\d+)$', EntryDetail.as_view()),
    url(r'', EntryList.as_view()),
)
