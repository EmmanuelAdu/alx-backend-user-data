#!/usr/bin/env python3
"""
Session_exp_auth module
"""

import os
from .session_auth import SessionAuth
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """
    SessionExpAuth class, inherits from SessionAuth
    This class is used to authenticate a user through session tokens
    with an expiration date
    """

    def __init__(self):
        super().__init__()
        self.session_duration = self._get_session_duration

    def _get_session_duration(self):
        """
        Get the duration of a session from
        the environment variable "SESSION_DURATION".

        Returns:
            int: The session duration in seconds. Defaults
            to 0 if the environment variable is not set or
            is not an integer.
        """
        session_duration = os.getenv("SESSION_DURATION")
        try:
            session_duration = int(session_duration)
        except (TypeError, ValueError):
            return 0
        return session_duration

    def create_session(self, user_id=None):
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        session_dict = {
            "user_id": user_id,
            "created_at": datetime.now
        }
        self.user_id_by_session_id[session_id] = session_dict
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Get the user ID associated with a session ID.

        Args:
            session_id (str): The session ID.

        Returns:
            str or None: The user ID associated with the session ID,
            or None if the session ID is not found or has expired.
        """
        if session_id is None:
            return None

        session_dict = self.user_id_by_session_id.get(session_id)

        if not session_dict:
            return None

        if self.session_cookie <= 0:
            return session_dict.get("user_id")

        created_at = session_dict.get("created_at")

        if not created_at:
            return None

        expiration_time = created_at + timedelta(seconds=self.session_duration)

        if datetime.now() > expiration_time:
            return None

        return session_dict.get("user_id")
