from rest_framework import pagination, renderers, serializers
from rest_framework_gis.serializers import (GeoModelSerializer,
                                            GeoFeatureModelSerializer)

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
        fields = ('id', 'name',)
        root_name = 'types'


class WrappingJSONRenderer(renderers.JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        root_name = getattr(renderer_context.get('view').get_serializer().Meta,
                            'root_name', None)
        if root_name:
            data = { root_name: data }
        return super(WrappingJSONRenderer, self).render(data,
                                                        accepted_media_type,
                                                        renderer_context)


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
                  'centroid', 'sectors', 'types', 'videos',)


class NextPageNumberField(serializers.Field):

    def to_native(self, value):
        return value.next_page_number()


class CurrentPageNumberField(serializers.Field):

    def to_native(self, value):
        return value.number


class MetaPaginationSerializer(serializers.Serializer):
    next_page = NextPageNumberField(source='*')
    current_page = CurrentPageNumberField(source='*')
    total_results = serializers.Field(source='paginator.count')


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
