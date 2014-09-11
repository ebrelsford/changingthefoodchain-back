from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt

from .views import ContactView


urlpatterns = patterns('',
    url(r'', csrf_exempt(ContactView.as_view())),
)
