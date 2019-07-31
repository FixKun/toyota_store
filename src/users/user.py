"""
Base user class
"""
import uuid
import secrets
from api import login
from sqlalchemy import (
    Column,
    ForeignKey,
    String,
    Boolean
)
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID
from api import db
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)


class User(UserMixin, db.Model):
    """Base user class"""

    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True),
                unique=True,
                primary_key=True,
                default=lambda: str(uuid.uuid4()))
    username = Column(String,
                      unique=True,
                      nullable=False)
    password = Column(String,
                      nullable=False)
    admin = Column(Boolean)
    api_token = Column(String,
                       unique=True,
                       nullable=False,
                       default=lambda: secrets.token_urlsafe(20))

    def __init__(self, username, admin=False):
        self.username = username
        self.admin = admin

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @login.user_loader
    def load_user(username):
        return User.query.filter_by(username=username).first()