"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import areainfo as shared_areainfo
from typing import Optional


@dataclasses.dataclass
class GetAreaInfoV3OrderAreaInfoGetRequest:
    zip_code: str = dataclasses.field(metadata={'query_param': { 'field_name': 'zip_code', 'style': 'form', 'explode': True }})
    r"""Zip code of the area to check"""
    



@dataclasses.dataclass
class GetAreaInfoV3OrderAreaInfoGetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    area_info: Optional[shared_areainfo.AreaInfo] = dataclasses.field(default=None)
    r"""Successful Response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

