from rest_framework import generics, mixins, renderers

from content.serializers import PhotoSerializer, VideoSerializer

from handthatfeeds.api import WrappingJSONRenderer
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
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    renderer_classes = (WrappingJSONRenderer, renderers.BrowsableAPIRenderer)


class OrganizationNameList(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationNameSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class OrganizationGeoJSONList(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationGeoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class OrganizationList(mixins.ListModelMixin, mixins.CreateModelMixin,
                       generics.GenericAPIView):
    model = Organization
    paginate_by = 50
    pagination_serializer_class = PaginatedOrganizationSerializer

    def get_queryset(self):
        qs = Organization.objects.all()
        sortby = self.request.QUERY_PARAMS.get('sortby', 'name')
        sectors = self.request.QUERY_PARAMS.get('sectors', None)
        types = self.request.QUERY_PARAMS.get('types', None)

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
