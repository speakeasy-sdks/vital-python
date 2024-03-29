"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import getordersresponse as shared_getordersresponse
from datetime import datetime
from typing import List, Optional


@dataclasses.dataclass
class GetOrdersV3OrdersGetRequest:
    end_date: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'end_date', 'style': 'form', 'explode': True }})
    r"""Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59"""
    order_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'order_ids', 'style': 'form', 'explode': True }})
    r"""Filter by order ids."""
    page: Optional[int] = dataclasses.field(default=1, metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    patient_name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'patient_name', 'style': 'form', 'explode': True }})
    r"""Filter by patient name."""
    size: Optional[int] = dataclasses.field(default=50, metadata={'query_param': { 'field_name': 'size', 'style': 'form', 'explode': True }})
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'start_date', 'style': 'form', 'explode': True }})
    r"""Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00"""
    user_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'user_id', 'style': 'form', 'explode': True }})
    r"""Filter by user ID."""
    



@dataclasses.dataclass
class GetOrdersV3OrdersGetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    get_orders_response: Optional[shared_getordersresponse.GetOrdersResponse] = dataclasses.field(default=None)
    r"""Successful Response"""
    

