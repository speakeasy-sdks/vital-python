"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import clientfacinguser as shared_clientfacinguser
from typing import Optional



@dataclasses.dataclass
class SearchTeamUsersByUUIDOrClientUserIDV2TeamUsersSearchGetRequest:
    query_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query_id', 'style': 'form', 'explode': True }})
    




@dataclasses.dataclass
class SearchTeamUsersByUUIDOrClientUserIDV2TeamUsersSearchGetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    client_facing_users: Optional[list[shared_clientfacinguser.ClientFacingUser]] = dataclasses.field(default=None)
    r"""Successful Response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    
