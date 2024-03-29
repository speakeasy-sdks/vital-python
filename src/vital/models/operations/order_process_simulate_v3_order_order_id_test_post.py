"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import orderstatus as shared_orderstatus
from typing import Any, Optional


@dataclasses.dataclass
class OrderProcessSimulateV3OrderOrderIDTestPostRequest:
    order_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'order_id', 'style': 'simple', 'explode': False }})
    delay: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'delay', 'style': 'form', 'explode': True }})
    final_status: Optional[shared_orderstatus.OrderStatus] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'final_status', 'style': 'form', 'explode': True }})
    r"""An enumeration."""
    



@dataclasses.dataclass
class OrderProcessSimulateV3OrderOrderIDTestPostResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    response_order_process_simulate_v3_order_order_id_test_post: Optional[Any] = dataclasses.field(default=None)
    r"""Successful Response"""
    

