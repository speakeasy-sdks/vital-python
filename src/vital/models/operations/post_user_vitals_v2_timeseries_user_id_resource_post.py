"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import ingestibletimeseriesresource as shared_ingestibletimeseriesresource
from typing import Optional


@dataclasses.dataclass
class PostUserVitalsV2TimeseriesUserIDResourcePostRequest:
    resource: shared_ingestibletimeseriesresource.IngestibleTimeseriesResource = dataclasses.field(metadata={'path_param': { 'field_name': 'resource', 'style': 'simple', 'explode': False }})
    r"""An enumeration."""
    user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'user_id', 'style': 'simple', 'explode': False }})
    x_vital_android_sdk_version: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'x-vital-android-sdk-version', 'style': 'simple', 'explode': False }})
    x_vital_ios_sdk_version: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'x-vital-ios-sdk-version', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class PostUserVitalsV2TimeseriesUserIDResourcePostResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    response_post_user_vitals_v2_timeseries_user_id_resource_post: Optional[str] = dataclasses.field(default=None)
    r"""Successful Response"""
    

