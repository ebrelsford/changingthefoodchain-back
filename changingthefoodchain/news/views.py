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
        def category_dict(c):
            d = {
                'id': c.pk,
                'name': c.translations.get(language_code='en').title,
                'name_es': c.translations.get(language_code='es').title,
            }
            return d

        response = self.render_json_response({
            'categories': [category_dict(category) for category in
                           self.get_queryset()],
        })
        response['Allow'] = 'GET, HEAD, OPTIONS'
        return response


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

        categories = self.request.QUERY_PARAMS.get('category', None)
        featured = self.request.QUERY_PARAMS.get('featured', None)

        if categories:
            qs = qs.filter(categories__in=categories.split(','))
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
