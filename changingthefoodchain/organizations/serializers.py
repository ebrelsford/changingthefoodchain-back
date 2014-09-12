from rest_framework import pagination, serializers
from rest_framework_gis.serializers import (GeoModelSerializer,
                                            GeoFeatureModelSerializer)

from changingthefoodchain.api import MetaPaginationSerializer
from content.models import Photo, Video
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
    displayName = serializers.SerializerMethodField('get_display_name')

    def get_display_name(self, obj):
        location = None
        if obj.city or obj.state_province:
            locations = filter(lambda x: x is not None, [obj.city, obj.state_province])
            location = ', '.join(locations)
        if location:
            return '%s (%s)' % (obj.name, location)
        return obj.name

    class Meta:
        model = Organization
        root_name = 'organization'
        fields = ('id', 'name', 'displayName',)


class OrganizationSerializer(GeoModelSerializer):
    """Serializer for outputting a single organization"""
    photos = serializers.SerializerMethodField('get_photos')
    sectors = SectorSerializer(many=True,)
    types = TypeSerializer(many=True,)
    videos = serializers.SerializerMethodField('get_videos')

    def get_photos(self, obj):
        photos = Photo.objects.filter(organization=obj, visible=True)
        return PhotoSerializer(photos).data

    def get_videos(self, obj):
        videos = Video.objects.filter(organization=obj, visible=True)
        return VideoSerializer(videos).data

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
        fields = ('id', 'name', 'email', 'phone', 'address_line1',
                  'address_line2', 'city', 'state_province', 'postal_code',
                  'country', 'sectors', 'types', 'site_url', 'mission',)
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
