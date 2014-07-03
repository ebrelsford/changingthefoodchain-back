from django.conf.urls import patterns, url

from .views import OrganizationList


urlpatterns = patterns('',
    url(r'', OrganizationList.as_view()),
)
