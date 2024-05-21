#!/usr/bin/env python3
"""
Auth module
"""

from flask import request
from typing import List


class Auth:
    """
    Class for authentication.
    """

    def require_auth(
            self,
            path: str,
            excluded_paths: List[str]
    ) -> bool:
        """
        Checks if the path requires authentication.

        Args:
            path (str): The path to check.
            excluded_paths (List[str]): List of paths to exclude from
                requiring authentication.

        Returns:
            bool: True if the path requires authentication, False otherwise.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns the authorization header.

        Args:
            request (flask.Request): The flask Request object.

        Returns:
            str: The authorization header.
        """
        return None

    def current_user(self, request=None) -> str:
        """
        Returns the current user.

        Args:
            request (flask.Request): The flask Request object.

        Returns:
            str: The current user.
        """
        return None
