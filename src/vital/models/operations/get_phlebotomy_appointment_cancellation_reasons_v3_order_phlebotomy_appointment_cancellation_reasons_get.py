"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import clientfacingappointmentcancellationreason as shared_clientfacingappointmentcancellationreason
from typing import List, Optional


@dataclasses.dataclass
class GetPhlebotomyAppointmentCancellationReasonsV3OrderPhlebotomyAppointmentCancellationReasonsGetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    response_get_phlebotomy_appointment_cancellation_reasons_v3_order_phlebotomy_appointment_cancellation_reasons_get: Optional[List[shared_clientfacingappointmentcancellationreason.ClientFacingAppointmentCancellationReason]] = dataclasses.field(default=None)
    r"""Successful Response"""
    

