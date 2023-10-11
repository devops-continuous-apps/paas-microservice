from ..models.blacklist_entry import BlacklistEntry
from .base_command import BaseCommand


class CheckBlacklistCommand(BaseCommand):
    def __init__(self, email):
        self.email = email

    def execute(self):
        # Check if the email is in the blacklist
        entry = BlacklistEntry.query.filter_by(email=self.email).first()

        if entry:
            return True, entry.blocked_reason
        else:
            return False, None
