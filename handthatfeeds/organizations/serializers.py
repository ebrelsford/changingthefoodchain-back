from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Organization


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ('id', 'name', 'address_line1', 'city', 'state_province',
                  'postal_code', 'country',)


class OrganizationGeoSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Organization
        fields = ('id', 'name', 'address_line1', 'city', 'state_province',
                  'postal_code', 'country',)
        geo_field = 'centroid'
