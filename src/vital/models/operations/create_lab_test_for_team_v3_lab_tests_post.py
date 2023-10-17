"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import clientfacinglabtest as shared_clientfacinglabtest
from typing import Optional


@dataclasses.dataclass
class CreateLabTestForTeamV3LabTestsPostResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    client_facing_lab_test: Optional[shared_clientfacinglabtest.ClientFacingLabTest] = dataclasses.field(default=None)
    r"""Successful Response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

