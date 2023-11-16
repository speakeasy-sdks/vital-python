"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class PostUserProfileV2SummaryProfileUserIDPostRequest:
    user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'user_id', 'style': 'simple', 'explode': False }})
    x_vital_android_sdk_version: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'x-vital-android-sdk-version', 'style': 'simple', 'explode': False }})
    x_vital_ios_sdk_version: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'x-vital-ios-sdk-version', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class PostUserProfileV2SummaryProfileUserIDPostResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    response_post_user_profile_v2_summary_profile_user_id_post: Optional[str] = dataclasses.field(default=None)
    r"""Successful Response"""
    

