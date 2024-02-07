"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import clientfacingstepstimeseries as shared_clientfacingstepstimeseries
from typing import List, Optional


@dataclasses.dataclass
class GetTimeseriesResourceDataV2TimeseriesUserIDStepsGetRequest:
    start_date: str = dataclasses.field(metadata={'query_param': { 'field_name': 'start_date', 'style': 'form', 'explode': True }})
    r"""Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00"""
    user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'user_id', 'style': 'simple', 'explode': False }})
    end_date: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'end_date', 'style': 'form', 'explode': True }})
    r"""Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59"""
    provider: Optional[str] = dataclasses.field(default='', metadata={'query_param': { 'field_name': 'provider', 'style': 'form', 'explode': True }})
    r"""Provider oura/strava etc"""
    



@dataclasses.dataclass
class GetTimeseriesResourceDataV2TimeseriesUserIDStepsGetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    response_get_timeseries_resource_data_v2_timeseries_user_id_steps_get: Optional[List[shared_clientfacingstepstimeseries.ClientFacingStepsTimeseries]] = dataclasses.field(default=None)
    r"""Successful Response"""
    

