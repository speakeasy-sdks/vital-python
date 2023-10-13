"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import apikeyindb as shared_apikeyindb
from typing import Optional



@dataclasses.dataclass
class RotateAPIKeyV2TeamTeamIDApikeyAPIKeyIDRotatePatchRequest:
    api_key_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'api_key_id', 'style': 'simple', 'explode': False }})
    team_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'team_id', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class RotateAPIKeyV2TeamTeamIDApikeyAPIKeyIDRotatePatchResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    api_key_in_db: Optional[shared_apikeyindb.APIKeyInDB] = dataclasses.field(default=None)
    r"""Successful Response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

