"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import clientworkoutresponse as shared_clientworkoutresponse
from typing import Optional



@dataclasses.dataclass
class GetUserWorkoutsV2SummaryWorkoutsUserIDGetRequest:
    start_date: str = dataclasses.field(metadata={'query_param': { 'field_name': 'start_date', 'style': 'form', 'explode': True }})
    r"""Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00"""
    user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'user_id', 'style': 'simple', 'explode': False }})
    end_date: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'end_date', 'style': 'form', 'explode': True }})
    r"""Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59"""
    provider: Optional[str] = dataclasses.field(default='', metadata={'query_param': { 'field_name': 'provider', 'style': 'form', 'explode': True }})
    r"""Provider oura/strava etc"""
    




@dataclasses.dataclass
class GetUserWorkoutsV2SummaryWorkoutsUserIDGetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    client_workout_response: Optional[shared_clientworkoutresponse.ClientWorkoutResponse] = dataclasses.field(default=None)
    r"""Successful Response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

