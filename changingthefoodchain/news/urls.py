from django.conf.urls import patterns, include, url

from elephantblog.urls import elephantblog_patterns


urlpatterns = patterns('',
    url(r'', include(elephantblog_patterns(
        list_kwargs={'only_active_language': False},
    ))),
)
