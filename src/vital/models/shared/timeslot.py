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
class TimeSlot:
    end: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""Time is in UTC"""
    is_priority: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_priority') }})
    num_appointments_available: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('num_appointments_available') }})
    price: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('price') }})
    start: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""Time is in UTC"""
    booking_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('booking_key'), 'exclude': lambda f: f is None }})
    expires_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expires_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    

