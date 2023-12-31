"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .appointmentprovider import AppointmentProvider
from .appointmentstatus import AppointmentStatus
from .appointmenttype import AppointmentType
from .lnglat import LngLat
from .usaddress import USAddress
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ClientFacingAppointment:
    address: USAddress = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address') }})
    can_reschedule: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('can_reschedule') }})
    end_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""Time is in UTC"""
    iana_timezone: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iana_timezone') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    location: LngLat = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('location') }})
    provider: AppointmentProvider = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provider') }})
    r"""An enumeration."""
    provider_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provider_id') }})
    start_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""Time is in UTC"""
    status: AppointmentStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""An enumeration."""
    type: AppointmentType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""An enumeration."""
    user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_id') }})
    

