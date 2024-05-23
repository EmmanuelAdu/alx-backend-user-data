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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Retrieves the USER ID based on the Session ID
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> str:
        """Returns a User instance based on a cookie value
        """
        session_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_cookie)
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """_summary_

        Args:
            request (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        if request is None:
            return False
        session_cookie = self.session_cookie(request)
        if session_cookie is None:
            return False
        user_id = self.user_id_for_session_id(session_cookie)
        if user_id is None:
            return False
        del self.user_id_by_session_id[session_cookie]
        return True
