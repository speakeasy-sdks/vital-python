"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class SourceAuthType(str, Enum):
    r"""An enumeration."""
    OAUTH = 'oauth'
    TEAM_OAUTH = 'team_oauth'
    SDK = 'sdk'
    PASSWORD = 'password'
    EMAIL = 'email'
    APP = 'app'
    UNKNOWN = ''
