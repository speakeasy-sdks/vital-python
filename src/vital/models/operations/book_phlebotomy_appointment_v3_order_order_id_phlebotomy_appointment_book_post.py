"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import appointmentbookingrequest as shared_appointmentbookingrequest
from ..shared import clientfacingappointment as shared_clientfacingappointment
from typing import Optional



@dataclasses.dataclass
class BookPhlebotomyAppointmentV3OrderOrderIDPhlebotomyAppointmentBookPostRequest:
    appointment_booking_request: shared_appointmentbookingrequest.AppointmentBookingRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    order_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'order_id', 'style': 'simple', 'explode': False }})
    r"""Your Order ID."""
    




@dataclasses.dataclass
class BookPhlebotomyAppointmentV3OrderOrderIDPhlebotomyAppointmentBookPostResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    client_facing_appointment: Optional[shared_clientfacingappointment.ClientFacingAppointment] = dataclasses.field(default=None)
    r"""Successful Response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    
