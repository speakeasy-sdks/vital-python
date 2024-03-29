"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class ConnectProviderV2LinkConnectProviderGetRequest:
    provider: str = dataclasses.field(metadata={'path_param': { 'field_name': 'provider', 'style': 'simple', 'explode': False }})
    r"""Provider slug. e.g., `oura`, `fitbit`, `garmin`."""
    x_vital_sdk_no_redirect: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'x-vital-sdk-no-redirect', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class ConnectProviderV2LinkConnectProviderGetResponseConnectProviderV2LinkConnectProviderGet:
    r"""Successful Response"""
    



@dataclasses.dataclass
class ConnectProviderV2LinkConnectProviderGetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    response_connect_provider_v2_link_connect_provider_get: Optional[ConnectProviderV2LinkConnectProviderGetResponseConnectProviderV2LinkConnectProviderGet] = dataclasses.field(default=None)
    r"""Successful Response"""
    

