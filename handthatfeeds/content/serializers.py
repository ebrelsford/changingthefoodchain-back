from rest_framework import serializers

from .models import Photo, Video


class PhotoSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField('get_url')

    def get_url(self, obj):
        return '%s' % (obj.photo.url)

    class Meta:
        model = Photo
        fields = ('organization', 'photo', 'url',)


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ('organization', 'url',)
