from django.conf import settings
from django.views.generic import ListView

from braces.views import JSONResponseMixin
from elephantblog.models import Category, Entry
from rest_framework import generics, renderers

from changingthefoodchain.api import WrappingJSONRenderer
from .serializers import (EntrySerializer, EntryGeoSerializer,
                          PaginatedEntrySerializer)


class CategoryList(JSONResponseMixin, ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        default_language = settings.LANGUAGE_CODE
        language = request.GET.get('language', default_language)
        def category_dict(c):
            d = {
                'id': c.pk,
            }
            try:
                d['name'] = c.translations.get(language_code=language).title
            except Exception:
                d['name'] = c.translations.get(language_code=default_language).title
            return d

        return self.render_json_response({
            'categories': [category_dict(category) for category in
                           self.get_queryset()],
        })


class EntryGeoJSONList(generics.ListAPIView):
    serializer_class = EntryGeoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        return Entry.objects.filter(is_active=True)


class EntryList(generics.ListAPIView):
    model = Entry
    paginate_by = 20
    pagination_serializer_class = PaginatedEntrySerializer
    serializer_class = EntrySerializer

    def get_queryset(self):
        qs = Entry.objects.filter(is_active=True)

        category = self.request.QUERY_PARAMS.get('category', None)
        featured = self.request.QUERY_PARAMS.get('featured', None)

        if category:
            qs = qs.filter(categories=category)
        if featured and featured.lower() == 'true':
            qs = qs.filter(is_featured=True)

        # Filter by language
        language = self.request.QUERY_PARAMS.get('language', 'en')
        if language:
            qs = qs.filter(language=language)

        return qs.order_by('-published_on')


class EntryDetail(generics.RetrieveAPIView):
    model = Entry
    renderer_classes = (WrappingJSONRenderer, renderers.BrowsableAPIRenderer)
    serializer_class = EntrySerializer
