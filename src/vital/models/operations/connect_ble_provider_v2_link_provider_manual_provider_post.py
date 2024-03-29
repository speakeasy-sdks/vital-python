"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import manualconnectiondata as shared_manualconnectiondata
from enum import Enum
from typing import Dict, Optional

class ProvidersThatAreManuallyAddedDevicesSuchAsBleDevicesAndGeneratedData(str, Enum):
    r"""An enumeration."""
    BEURER_BLE = 'beurer_ble'
    OMRON_BLE = 'omron_ble'
    ACCUCHEK_BLE = 'accuchek_ble'
    CONTOUR_BLE = 'contour_ble'
    FREESTYLE_LIBRE_BLE = 'freestyle_libre_ble'
    ONETOUCH_BLE = 'onetouch_ble'
    APPLE_HEALTH_KIT = 'apple_health_kit'
    MANUAL = 'manual'
    HEALTH_CONNECT = 'health_connect'


@dataclasses.dataclass
class ConnectBleProviderV2LinkProviderManualProviderPostRequest:
    manual_connection_data: shared_manualconnectiondata.ManualConnectionData = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    provider: ProvidersThatAreManuallyAddedDevicesSuchAsBleDevicesAndGeneratedData = dataclasses.field(metadata={'path_param': { 'field_name': 'provider', 'style': 'simple', 'explode': False }})
    r"""An enumeration."""
    



@dataclasses.dataclass
class ConnectBleProviderV2LinkProviderManualProviderPostResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    response_connect_ble_provider_v2_link_provider_manual_provider_post: Optional[Dict[str, bool]] = dataclasses.field(default=None)
    r"""Successful Response"""
    

