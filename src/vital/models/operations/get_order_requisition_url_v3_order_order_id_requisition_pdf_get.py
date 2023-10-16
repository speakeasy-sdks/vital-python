"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional



@dataclasses.dataclass
class GetOrderRequisitionURLV3OrderOrderIDRequisitionPdfGetRequest:
    order_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'order_id', 'style': 'simple', 'explode': False }})
    r"""Your Order ID."""
    




@dataclasses.dataclass
class GetOrderRequisitionURLV3OrderOrderIDRequisitionPdfGetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    get_order_requisition_url_v3_order_order_id_requisition_pdf_get_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    r"""Successful Response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    
