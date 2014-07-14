from rest_framework import generics, mixins

from content.serializers import PhotoSerializer, VideoSerializer

from .models import Organization
from .serializers import (OrganizationAddSerializer, OrganizationSerializer,
                          OrganizationGeoSerializer)


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


class OrganizationGeoJSONList(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationGeoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class OrganizationList(mixins.ListModelMixin, mixins.CreateModelMixin,
                       generics.GenericAPIView):
    queryset = Organization.objects.all().order_by('name')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OrganizationAddSerializer
        return OrganizationSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
