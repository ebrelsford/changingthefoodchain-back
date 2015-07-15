from feincms_oembed.providers import embedly_oembed_provider


def minimalist(url, kwargs):
    """
    Attempt to remove branding and titles from youtube and vimeo videos, other
    types of content should be embedded as usual.
    """
    kwargs.update({
        'vimeo_badge': 0,
        'vimeo_byline': 0,
        'vimeo_portrait': 0,
        'vimeo_title': 0,
        'youtube_modestbranding': 1,
        'youtube_rel': 0,
        'youtube_showinfo': 0
    })
    return embedly_oembed_provider(url, kwargs)
