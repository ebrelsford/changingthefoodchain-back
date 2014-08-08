from django.conf.urls import patterns, include, url

from elephantblog.urls import elephantblog_patterns


urlpatterns = patterns('',
    url(r'^blog/', include(elephantblog_patterns(
        list_kwargs={'only_active_language': False},
    ))),
)
