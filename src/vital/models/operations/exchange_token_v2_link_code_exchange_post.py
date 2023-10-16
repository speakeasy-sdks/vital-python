"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import vitaltokenexchangeresponse as shared_vitaltokenexchangeresponse
from typing import Optional



@dataclasses.dataclass
class ExchangeTokenV2LinkCodeExchangePostRequest:
    code: str = dataclasses.field(metadata={'query_param': { 'field_name': 'code', 'style': 'form', 'explode': True }})
    




@dataclasses.dataclass
class ExchangeTokenV2LinkCodeExchangePostResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    vital_token_exchange_response: Optional[shared_vitaltokenexchangeresponse.VitalTokenExchangeResponse] = dataclasses.field(default=None)
    r"""Successful Response"""
    
