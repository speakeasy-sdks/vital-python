"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional



@dataclasses.dataclass
class UpdateSourcePrioritiesV2TeamSourcePrioritiesPatchRequest:
    team_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'team_id', 'style': 'form', 'explode': True }})
    




@dataclasses.dataclass
class UpdateSourcePrioritiesV2TeamSourcePrioritiesPatch200ApplicationJSON:
    pass



@dataclasses.dataclass
class UpdateSourcePrioritiesV2TeamSourcePrioritiesPatchResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    update_source_priorities_v2_team_source_priorities_patch_200_application_json_objects: Optional[list[UpdateSourcePrioritiesV2TeamSourcePrioritiesPatch200ApplicationJSON]] = dataclasses.field(default=None)
    r"""Successful Response"""
    
