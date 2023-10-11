"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import rawprofile as shared_rawprofile
from typing import Optional



@dataclasses.dataclass
class GetUserProfileRawV2SummaryProfileUserIDRawGetRequest:
    user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'user_id', 'style': 'simple', 'explode': False }})
    provider: Optional[str] = dataclasses.field(default='', metadata={'query_param': { 'field_name': 'provider', 'style': 'form', 'explode': True }})
    r"""Provider oura/strava etc"""
    




@dataclasses.dataclass
class GetUserProfileRawV2SummaryProfileUserIDRawGetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_profile: Optional[shared_rawprofile.RawProfile] = dataclasses.field(default=None)
    r"""Successful Response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

