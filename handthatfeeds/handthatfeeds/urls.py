from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^content/', include('content.urls')),

    # Django REST Framework
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),

    # FeinCMS
    url(r'', include('feincms.urls')),
) + (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
    (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)))
