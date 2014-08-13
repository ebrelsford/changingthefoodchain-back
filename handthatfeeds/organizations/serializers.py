from rest_framework import pagination, serializers
from rest_framework_gis.serializers import (GeoModelSerializer,
                                            GeoFeatureModelSerializer)

from handthatfeeds.api import MetaPaginationSerializer
from content.serializers import PhotoSerializer, VideoSerializer
from .models import Organization, Sector, Type


class SectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sector
        fields = ('id', 'name',)
        root_name = 'sectors'


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = ('id', 'name', 'description', 'image',)
        root_name = 'types'


class OrganizationNameSerializer(serializers.ModelSerializer):
    """Serializer for outputting organizations' names"""

    class Meta:
        model = Organization
        root_name = 'organization'
        fields = ('id', 'name',)


class OrganizationSerializer(GeoModelSerializer):
    """Serializer for outputting a single organization"""
    photos = PhotoSerializer(many=True, source='photo_set')
    sectors = SectorSerializer(many=True,)
    types = TypeSerializer(many=True,)
    videos = VideoSerializer(many=True, source='video_set')

    class Meta:
        model = Organization
        root_name = 'organization'
        fields = ('id', 'name', 'email', 'phone', 'address_line1', 'city',
                  'state_province', 'postal_code', 'country', 'photos',
                  'centroid', 'sectors', 'types', 'videos', 'site_url',
                  'mission',)


class PaginatedOrganizationSerializer(pagination.BasePaginationSerializer):
    model = Organization
    results_field = 'organizations'
    meta = MetaPaginationSerializer(source='*')


class OrganizationAddSerializer(GeoFeatureModelSerializer):
    """Serializer for adding a new organization"""
    sectors = serializers.SlugRelatedField(many=True, slug_field='name')
    types = serializers.SlugRelatedField(many=True, slug_field='name')

    class Meta:
        model = Organization
        fields = ('id', 'name', 'email', 'phone', 'address_line1', 'city',
                  'state_province', 'postal_code', 'country', 'sectors',
                  'types', 'site_url', 'mission',)
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
