from rest_framework import serializers

from .models import Photo, Video


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ('organization', 'photo',)


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ('organization', 'url',)
