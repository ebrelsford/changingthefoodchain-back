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
    """Serializer for outputting a single organization"""
    photos = PhotoSerializer(many=True, source='photo_set')
    sectors = SectorSerializer(many=True,)
    types = TypeSerializer(many=True,)

    class Meta:
        model = Organization
        fields = ('id', 'name', 'email', 'phone', 'address_line1', 'city',
                  'state_province', 'postal_code', 'country', 'photos',
                  'sectors', 'types',)


class OrganizationAddSerializer(GeoFeatureModelSerializer):
    """Serializer for adding a new organization"""
    sectors = serializers.SlugRelatedField(many=True, slug_field='name')
    types = serializers.SlugRelatedField(many=True, slug_field='name')

    class Meta:
        model = Organization
        fields = ('id', 'name', 'email', 'phone', 'address_line1', 'city',
                  'state_province', 'postal_code', 'country',
                  'sectors', 'types',)
        geo_field = 'centroid'


class OrganizationGeoSerializer(GeoFeatureModelSerializer):
    """Serializer for outputting organizations as GeoJSON"""
    sectors = serializers.SlugRelatedField(many=True, read_only=True,
                                           slug_field='name')
    types = serializers.SlugRelatedField(many=True, read_only=True,
                                         slug_field='name')
    class Meta:
        model = Organization
        fields = ('id', 'name', 'sectors', 'types',)
        geo_field = 'centroid'
