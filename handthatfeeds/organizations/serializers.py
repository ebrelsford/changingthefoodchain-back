from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from content.serializers import PhotoSerializer
from .models import Organization, Sector, Type


class SectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sector
        fields = ('id', 'name',)


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = ('id', 'name',)


class OrganizationSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, source='photo_set')
    sectors = SectorSerializer(many=True,)
    types = TypeSerializer(many=True,)

    class Meta:
        model = Organization
        fields = ('id', 'name', 'email', 'phone', 'address_line1', 'city',
                  'state_province', 'postal_code', 'country', 'photos',
                  'sectors', 'types',)


class OrganizationGeoSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Organization
        fields = ('id', 'name', 'address_line1', 'city', 'state_province',
                  'postal_code', 'country',)
        geo_field = 'centroid'
