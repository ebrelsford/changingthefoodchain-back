from moderation.moderator import GenericModerator


class StandardModerator(GenericModerator):
    auto_reject_for_anonymous = False
    bypass_moderation_after_approval = True
    notify_user = False
    visibility_column = 'visible'
    visible_until_rejected = False
