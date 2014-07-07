from rest_framework import generics, mixins

from content.serializers import PhotoSerializer, VideoSerializer

from .models import Organization
from .serializers import OrganizationSerializer, OrganizationGeoSerializer


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


class OrganizationList(mixins.ListModelMixin, mixins.CreateModelMixin,
                       generics.GenericAPIView):

    queryset = Organization.objects.all()
    serializer_class = OrganizationGeoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
