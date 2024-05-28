#!/usr/bin/env python3
"""User Model
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class User(Base):
    """
    Represents a user of the system.

    Attributes:
        id (Integer): Unique identifier for the user.
        email (String): User's email address.
        hashed_password (String): Hashed version of the user's password.
        session_id (String): Unique identifier for the user's session.
        reset_token (String): Token used to reset the user's password.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
