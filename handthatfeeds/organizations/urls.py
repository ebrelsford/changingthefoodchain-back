from django.conf.urls import patterns, url

from .views import OrganizationDetail, OrganizationList


urlpatterns = patterns('',
    url(r'(?P<pk>\d+)', OrganizationDetail.as_view()),
    url(r'', OrganizationList.as_view()),
)
