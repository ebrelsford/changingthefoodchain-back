from rest_framework import pagination, serializers

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


class EntrySerializer(serializers.ModelSerializer):
    cover = RegionField(region='cover', source='content')
    main = RegionField(region='main', source='content')
    preview = RegionField(region='preview', source='content')

    class Meta:
        model = Entry
        fields = ('id', 'title', 'author', 'published_on', 'preview', 'main',
                  'cover', 'categories', 'link', 'read_more_at',)
        root_name = 'entries'


class PaginatedEntrySerializer(pagination.BasePaginationSerializer):
    model = Entry
    results_field = 'entries'
    meta = MetaPaginationSerializer(source='*')
