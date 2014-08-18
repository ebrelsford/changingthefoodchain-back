from moderation import moderation

from handthatfeeds.moderator import StandardModerator
from .models import Organization


class OrganizationModerator(StandardModerator):
    pass


moderation.register(Organization, OrganizationModerator)
