from rest_framework import generics, mixins

from .models import Organization
from .serializers import OrganizationSerializer, OrganizationGeoSerializer


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
