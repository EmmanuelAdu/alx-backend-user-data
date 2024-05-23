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
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        if path in excluded_paths:
            return False
        for excluded_path in excluded_paths:
            if excluded_path.startswith(path):
                return False
            elif path.startswith(excluded_path):
                return False
            elif excluded_path[-1] == "*":
                if path.startswith(excluded_path[:-1]):
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns the authorization header.

        Args:
            request (flask.Request): The flask Request object.

        Returns:
            str: The authorization header.
        """
        if request is None:
            return None

        header = request.headers.get("Authorization")
        if header is None:
            return None

        return header

    def current_user(self, request=None) -> str:
        """
        Returns the current user.

        Args:
            request (flask.Request): The flask Request object.

        Returns:
            str: The current user.
        """
        return None
