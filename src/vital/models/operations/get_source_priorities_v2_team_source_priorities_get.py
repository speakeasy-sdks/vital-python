"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional



@dataclasses.dataclass
class GetSourcePrioritiesV2TeamSourcePrioritiesGetRequest:
    data_type: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'data_type', 'style': 'form', 'explode': True }})
    




@dataclasses.dataclass
class GetSourcePrioritiesV2TeamSourcePrioritiesGet200ApplicationJSON:
    pass



@dataclasses.dataclass
class GetSourcePrioritiesV2TeamSourcePrioritiesGetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    get_source_priorities_v2_team_source_priorities_get_200_application_json_objects: Optional[list[GetSourcePrioritiesV2TeamSourcePrioritiesGet200ApplicationJSON]] = dataclasses.field(default=None)
    r"""Successful Response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    
