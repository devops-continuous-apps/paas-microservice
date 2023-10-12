from sqlalchemy import Column, String, DateTime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid
from marshmallow import Schema, fields

db = SQLAlchemy()


class BlacklistEntry(db.Model):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False)
    app_uuid = Column(UUID(as_uuid=True), nullable=False)
    blocked_reason = Column(String(length=255))
    created_at = Column(DateTime)
    source_ip = Column(String)


class BlacklistEntrySchema(Schema):
    id = fields.UUID()
    email = fields.Str()
    app_uuid = fields.UUID()
    blocked_reason = fields.Str()
    created_at = fields.DateTime()
    source_ip = fields.Str()
