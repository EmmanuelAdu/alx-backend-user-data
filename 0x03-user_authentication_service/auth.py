#!/usr/bin/env python3
"""
Auth module
"""

import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> str:
    """
    Hashes a password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
