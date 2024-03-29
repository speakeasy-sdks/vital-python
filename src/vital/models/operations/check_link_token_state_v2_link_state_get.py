"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class CheckLinkTokenStateV2LinkStateGetResponseCheckLinkTokenStateV2LinkStateGet:
    r"""Successful Response"""
    



@dataclasses.dataclass
class CheckLinkTokenStateV2LinkStateGetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    response_check_link_token_state_v2_link_state_get: Optional[CheckLinkTokenStateV2LinkStateGetResponseCheckLinkTokenStateV2LinkStateGet] = dataclasses.field(default=None)
    r"""Successful Response"""
    

