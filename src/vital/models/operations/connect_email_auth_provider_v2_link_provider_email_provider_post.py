"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import connectionstatus as shared_connectionstatus
from ..shared import emailproviderauthlink as shared_emailproviderauthlink
from enum import Enum
from typing import Optional

class ConnectEmailAuthProviderV2LinkProviderEmailProviderPostProviderEmailProviders(str, Enum):
    r"""An enumeration."""
    FREESTYLE_LIBRE = 'freestyle_libre'


@dataclasses.dataclass
class ConnectEmailAuthProviderV2LinkProviderEmailProviderPostRequest:
    email_provider_auth_link: shared_emailproviderauthlink.EmailProviderAuthLink = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    provider: ConnectEmailAuthProviderV2LinkProviderEmailProviderPostProviderEmailProviders = dataclasses.field(metadata={'path_param': { 'field_name': 'provider', 'style': 'simple', 'explode': False }})
    r"""An enumeration."""
    



@dataclasses.dataclass
class ConnectEmailAuthProviderV2LinkProviderEmailProviderPostResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    connection_status: Optional[shared_connectionstatus.ConnectionStatus] = dataclasses.field(default=None)
    r"""Successful Response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

