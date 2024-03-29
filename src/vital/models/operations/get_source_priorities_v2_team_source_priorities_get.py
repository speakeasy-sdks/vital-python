"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import List, Optional


@dataclasses.dataclass
class GetSourcePrioritiesV2TeamSourcePrioritiesGetRequest:
    data_type: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'data_type', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class ResponseBody:
    pass


@dataclasses.dataclass
class GetSourcePrioritiesV2TeamSourcePrioritiesGetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    response_get_source_priorities_v2_team_source_priorities_get: Optional[List[ResponseBody]] = dataclasses.field(default=None)
    r"""Successful Response"""
    

