#!/usr/bin/env python3
"""
Module for authentication using Basic Auth
"""


from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Class for authentication using Basic Auth
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Returns the Base64 part of the Authorization header
        for a Basic Auth
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        token = authorization_header.split(' ')[-1]
        return token
