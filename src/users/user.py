"""
Base user class
"""
from datetime import (
    datetime,
    timedelta
)
import uuid
import secrets
from app import (
    login,
    db)
from sqlalchemy import (
    Column,
    String,
    Boolean
)
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)


class User(UserMixin, db.Model):
    """ Base user class"""

    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True),
                unique=True,
                primary_key=True,
                default=lambda: str(uuid.uuid4()))
    username = Column(String,
                      unique=True,
                      nullable=False)
    __password = Column("password",
                        String,
                        nullable=False)
    admin = Column(Boolean)
    api_token = Column(String(32),
                       unique=True,
                       index=True,
                       nullable=False,
                       default=lambda: secrets.token_urlsafe(32))
    api_token_expiration = db.Column(db.DateTime)

    def __init__(self, username, admin=False):
        self.username = username
        self.admin = admin

    def set_password(self, password):
        self.__password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.__password, password)

    # Methods for handling tokens
    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.api_token and self.api_token_expiration and self.api_token_expiration > now + timedelta(seconds=60):
            return self.api_token
        self.api_token = secrets.token_urlsafe(32)
        self.api_token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.api_token

    def revoke_token(self):
        self.api_token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(api_token=token).first()
        if user is None or user.api_token_expiration < datetime.utcnow():
            return None
        return user

    # Flask stuff to find the user
    @login.user_loader
    def load_user(id):
        return User.query.get(id)
