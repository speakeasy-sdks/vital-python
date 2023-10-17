"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from typing import Optional
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ClientFacingTestkitOrderClientFacingShipment:
    r"""Schema for a Shipment in the client facing API.

    To be used as part of a ClientFacingTestkitOrder.
    """
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The Vital Shipment ID"""
    inbound_courier: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('inbound_courier'), 'exclude': lambda f: f is None }})
    r"""Courier used for delivery to lab"""
    inbound_tracking_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('inbound_tracking_number'), 'exclude': lambda f: f is None }})
    r"""Tracking number for delivery to lab"""
    inbound_tracking_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('inbound_tracking_url'), 'exclude': lambda f: f is None }})
    r"""Tracking url for delivery to lab"""
    notes: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('notes'), 'exclude': lambda f: f is None }})
    r"""Notes associated to the Vital shipment"""
    outbound_courier: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('outbound_courier'), 'exclude': lambda f: f is None }})
    r"""Courier used for delivery to customer"""
    outbound_tracking_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('outbound_tracking_number'), 'exclude': lambda f: f is None }})
    r"""Tracking number for delivery to customer"""
    outbound_tracking_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('outbound_tracking_url'), 'exclude': lambda f: f is None }})
    r"""Tracking url for delivery to customer"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ClientFacingTestkitOrder:
    r"""Schema for a testkit order in the client facing API.

    To be used as part of a ClientFacingOrder.
    """
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The Vital TestKit Order ID"""
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    shipment: Optional[ClientFacingTestkitOrderClientFacingShipment] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shipment'), 'exclude': lambda f: f is None }})
    r"""Shipment object"""
    

