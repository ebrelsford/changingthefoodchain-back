from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_page

from .views import (OrganizationCSV, OrganizationDetail,
                    OrganizationGeoJSONList, OrganizationNameList,
                    OrganizationPhotos, OrganizationVideos)


urlpatterns = patterns('',
    url(r'(?P<pk>\d+)/photos/', OrganizationPhotos.as_view()),
    url(r'(?P<pk>\d+)/videos/', OrganizationVideos.as_view()),
    url(r'(?P<pk>\d+)', OrganizationDetail.as_view()),
    url(r'csv/', OrganizationCSV.as_view()),
    url(r'geojson/', cache_page(60 * 60)(OrganizationGeoJSONList.as_view())),
    url(r'names/', OrganizationNameList.as_view()),
)
