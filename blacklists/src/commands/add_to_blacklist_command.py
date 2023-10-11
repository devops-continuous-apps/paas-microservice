from ..models.blacklist_entry import BlacklistEntry
from ..errors.errors import InvalidParams, EmailAlreadyExists
from ..models.blacklist_entry import db
from .base_command import BaseCommand


class AddToBlacklistCommand(BaseCommand):
    def __init__(self, email, app_uuid, blocked_reason=None):
        self.email = email
        self.app_uuid = app_uuid
        self.blocked_reason = blocked_reason

    def execute(self):
        if not self.email or not self.app_uuid:
            raise InvalidParams()

        # Check if the email is already in the blacklist
        existing_entry = BlacklistEntry.query.filter_by(email=self.email).first()
        if existing_entry:
            raise EmailAlreadyExists()

        # Create a new entry in the blacklist
        new_entry = BlacklistEntry(
            email=self.email,
            app_uuid=self.app_uuid,
            blocked_reason=self.blocked_reason
        )

        # Add the entry to the database
        db.session.add(new_entry)
        db.session.commit()

        return {
            'message': 'Email added to the blacklist'
        }
