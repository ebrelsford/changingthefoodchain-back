from django.conf.urls import patterns, url

from .views import (OrganizationDetail, OrganizationList, OrganizationPhotos,
                    OrganizationVideos)


urlpatterns = patterns('',
    url(r'(?P<pk>\d+)/photos/', OrganizationPhotos.as_view()),
    url(r'(?P<pk>\d+)/videos/', OrganizationVideos.as_view()),
    url(r'(?P<pk>\d+)', OrganizationDetail.as_view()),
    url(r'', OrganizationList.as_view()),
)
