from rest_framework import pagination, serializers
from rest_framework_gis.serializers import (GeoFeatureModelSerializer,
                                            GeoModelSerializer)

from elephantblog.models import Entry

from changingthefoodchain.api import MetaPaginationSerializer


class RegionField(serializers.Field):

    def __init__(self, *args, **kwargs):
        self.region = kwargs.pop('region')
        super(RegionField, self).__init__(*args, **kwargs)

    def to_native(self, value):
        context = {
            'full_path': self.context['request'].build_absolute_uri('/')[:-1],
        }
        return ''.join([c.render(**context) for c in getattr(value, self.region)])


class EntrySerializer(GeoModelSerializer):
    cover = RegionField(region='cover', source='content')
    main = RegionField(region='main', source='content')
    preview = RegionField(region='preview', source='content')

    class Meta:
        model = Entry
        fields = ('id', 'title', 'author', 'published_on', 'preview', 'main',
                  'cover', 'categories', 'link', 'read_more_at', 'location',)
        root_name = 'entries'


class EntryGeoSerializer(GeoFeatureModelSerializer):
    cover = RegionField(region='cover', source='content')

    class Meta:
        model = Entry
        fields = ('id', 'title', 'published_on', 'categories', 'is_featured',
                  'cover',)
        geo_field = 'location'


class PaginatedEntrySerializer(pagination.BasePaginationSerializer):
    model = Entry
    results_field = 'entries'
    meta = MetaPaginationSerializer(source='*')
