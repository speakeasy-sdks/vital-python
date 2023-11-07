"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import clientfacingpayorsearchresponse as shared_clientfacingpayorsearchresponse
from typing import List, Optional


@dataclasses.dataclass
class SearchInsurancePayorInformationV3InsuranceSearchPayorPostResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    response_search_insurance_payor_information_v3_insurance_search_payor_post: Optional[List[shared_clientfacingpayorsearchresponse.ClientFacingPayorSearchResponse]] = dataclasses.field(default=None)
    r"""Successful Response"""
    

