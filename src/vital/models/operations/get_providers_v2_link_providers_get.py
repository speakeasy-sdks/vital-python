"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import sourcelink as shared_sourcelink
from typing import List, Optional


@dataclasses.dataclass
class GetProvidersV2LinkProvidersGetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    response_get_providers_v2_link_providers_get: Optional[List[shared_sourcelink.SourceLink]] = dataclasses.field(default=None)
    r"""Successful Response"""
    

