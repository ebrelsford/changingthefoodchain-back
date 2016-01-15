from django.contrib.gis.geos import Polygon
from django.db.models import Q
from rest_framework import generics, mixins, renderers
from rest_framework.settings import api_settings
from rest_framework_csv.renderers import CSVRenderer

from content.serializers import PhotoSerializer, VideoSerializer

from changingthefoodchain.api import WrappingJSONRenderer
from .models import Organization, Sector, Type
from .serializers import (OrganizationAddSerializer, OrganizationSerializer,
                          OrganizationGeoSerializer, OrganizationNameSerializer,
                          PaginatedOrganizationSerializer, SectorSerializer,
                          TypeSerializer)


class OrganizationPhotos(generics.ListAPIView):
    serializer_class = PhotoSerializer

    def get_queryset(self):
        organization = Organization.objects.get(pk=self.kwargs.get('pk', None))
        return organization.photo_set.all()


class OrganizationVideos(generics.ListAPIView):
    serializer_class = VideoSerializer

    def get_queryset(self):
        organization = Organization.objects.get(pk=self.kwargs.get('pk', None))
        return organization.video_set.all()


class OrganizationDetail(generics.RetrieveAPIView):
    queryset = Organization.objects.filter(visible=True)
    serializer_class = OrganizationSerializer
    renderer_classes = (WrappingJSONRenderer, renderers.BrowsableAPIRenderer)


class OrganizationNameList(generics.ListAPIView):
    queryset = Organization.objects.filter(visible=True)
    serializer_class = OrganizationNameSerializer

    def get_queryset(self):
        qs = Organization.objects.all()
        q = self.request.QUERY_PARAMS.get('q')
        if (q):
            qs = qs.filter(
                Q(name__icontains=q) |
                Q(city__icontains=q) |
                Q(state_province__icontains=q)
            )
        return qs

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class OrganizationCSV(generics.ListAPIView):
    renderer_classes = [CSVRenderer,] + api_settings.DEFAULT_RENDERER_CLASSES
    serializer_class = OrganizationSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        return Organization.objects.all()


class OrganizationGeoJSONList(generics.ListAPIView):
    serializer_class = OrganizationGeoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        return Organization.objects.prefetch_related('sectors', 'types') \
                .filter(visible=True)


class OrganizationList(mixins.ListModelMixin, mixins.CreateModelMixin,
                       generics.GenericAPIView):
    model = Organization
    paginate_by = 50
    pagination_serializer_class = PaginatedOrganizationSerializer

    def get_queryset(self):
        qs = Organization.objects.filter(visible=True)
        bbox = self.request.QUERY_PARAMS.get('bbox', None)
        sortby = self.request.QUERY_PARAMS.get('sortby', 'name')
        sectors = self.request.QUERY_PARAMS.get('sectors', None)
        types = self.request.QUERY_PARAMS.get('types', None)

        if bbox:
            qs = qs.filter(centroid__within=Polygon.from_bbox(bbox.split(',')))
        if sectors:
            qs = qs.filter(sectors__name__in=sectors.split(','))
        if types:
            qs = qs.filter(types__name__in=types.split(','))
        return qs.order_by(sortby)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OrganizationAddSerializer
        return OrganizationSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


#
# Sectors
#


class SectorList(generics.ListAPIView):
    queryset = Sector.objects.all()
    renderer_classes = (WrappingJSONRenderer, renderers.BrowsableAPIRenderer)
    serializer_class = SectorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


#
# Types
#


class TypeList(generics.ListAPIView):
    queryset = Type.objects.all()
    renderer_classes = (WrappingJSONRenderer, renderers.BrowsableAPIRenderer)
    serializer_class = TypeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
