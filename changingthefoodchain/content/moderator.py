from moderation import moderation

from changingthefoodchain.moderator import StandardModerator
from .models import Photo, Video


class PhotoModerator(StandardModerator):
    pass


class VideoModerator(StandardModerator):
    pass


moderation.register(Photo, PhotoModerator)
moderation.register(Video, VideoModerator)
