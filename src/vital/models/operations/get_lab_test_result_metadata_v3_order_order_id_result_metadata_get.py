"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import labresultsmetadata as shared_labresultsmetadata
from typing import Optional


@dataclasses.dataclass
class GetLabTestResultMetadataV3OrderOrderIDResultMetadataGetRequest:
    order_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'order_id', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetLabTestResultMetadataV3OrderOrderIDResultMetadataGetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    lab_results_metadata: Optional[shared_labresultsmetadata.LabResultsMetadata] = dataclasses.field(default=None)
    r"""Successful Response"""
    

