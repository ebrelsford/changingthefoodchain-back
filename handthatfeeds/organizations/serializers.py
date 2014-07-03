from rest_framework_gis import serializers

from .models import Organization


class OrganizationSerializer(serializers.GeoFeatureModelSerializer):

    class Meta:
        model = Organization
        fields = ('name', 'address_line1', 'city', 'state_province',
                  'postal_code', 'country',)
        geo_field = 'centroid'
