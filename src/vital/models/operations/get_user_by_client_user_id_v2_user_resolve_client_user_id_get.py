"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import clientfacinguser as shared_clientfacinguser
from typing import Optional


@dataclasses.dataclass
class GetUserByClientUserIDV2UserResolveClientUserIDGetRequest:
    client_user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'client_user_id', 'style': 'simple', 'explode': False }})
    r"""A unique ID representing the end user. Typically this will be a user ID number from your application. Personally identifiable information, such as an email address or phone number, should not be used in the client_user_id."""
    



@dataclasses.dataclass
class GetUserByClientUserIDV2UserResolveClientUserIDGetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    client_facing_user: Optional[shared_clientfacinguser.ClientFacingUser] = dataclasses.field(default=None)
    r"""Successful Response"""
    

