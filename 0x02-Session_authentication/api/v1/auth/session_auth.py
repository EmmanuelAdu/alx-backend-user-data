#!/usr/bin/env python3
'''Module for authentication using Session Auth
'''


from .auth import Auth


from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    """Handles Session Authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Generate a Session ID for a User ID
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        id = uuid4()
        self.user_id_by_session_id[str(id)] = user_id
        return str(id)
