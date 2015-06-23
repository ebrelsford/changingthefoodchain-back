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
        fields = ('id', 'name', 'name_es',)
        root_name = 'sectors'


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = ('id', 'name', 'name_es', 'description', 'image',)
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
        return [PhotoSerializer(photo).data for photo in photos]

    def get_videos(self, obj):
        videos = Video.objects.filter(organization=obj, visible=True)
        return [VideoSerializer(video).data for video in videos]

    class Meta:
        model = Organization
        root_name = 'organization'
        fields = ('id', 'name', 'email', 'phone', 'address_line1', 'city',
                  'state_province', 'postal_code', 'country', 'photos',
                  'centroid', 'sectors', 'types', 'videos', 'site_url',
                  'mission', 'mission_es',)


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
    fcwa_organization = serializers.BooleanField(read_only=True)
    sectors = serializers.SlugRelatedField(many=True, read_only=True,
                                           slug_field='name')
    types = serializers.SlugRelatedField(many=True, read_only=True,
                                         slug_field='name')
    class Meta:
        model = Organization
        fields = ('id', 'name', 'fcwa_organization', 'sectors', 'types',)
        geo_field = 'centroid'
