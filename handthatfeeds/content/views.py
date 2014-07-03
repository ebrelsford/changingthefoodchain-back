from rest_framework import generics, mixins

from .models import Photo, Video
from .serializers import PhotoSerializer, VideoSerializer


class PhotoList(mixins.ListModelMixin, mixins.CreateModelMixin,
                generics.GenericAPIView):

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class VideoList(mixins.ListModelMixin, mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
