from rest_framework import renderers, serializers


class NextPageNumberField(serializers.Field):

    def to_native(self, value):
        try:
            return value.next_page_number()
        except Exception:
            return None


class CurrentPageNumberField(serializers.Field):

    def to_native(self, value):
        return value.number


class MetaPaginationSerializer(serializers.Serializer):
    next_page = NextPageNumberField(source='*')
    current_page = CurrentPageNumberField(source='*')
    total_results = serializers.Field(source='paginator.count')


class WrappingJSONRenderer(renderers.JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        root_name = getattr(renderer_context.get('view').get_serializer().Meta,
                            'root_name', None)
        if root_name:
            data = { root_name: data }
        return super(WrappingJSONRenderer, self).render(data,
                                                        accepted_media_type,
                                                        renderer_context)
