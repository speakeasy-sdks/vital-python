"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from typing import Any, Optional
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ClientFacingIgeTimeseries:
    UNSET='__SPEAKEASY_UNSET__'
    timestamp: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timestamp'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The timestamp of the measurement."""
    unit: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit') }})
    r"""Measured in FSU."""
    value: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    r"""The value of the measurement."""
    id: Optional[Any] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is ClientFacingIgeTimeseries.UNSET }})
    r"""Deprecated"""
    timezone_offset: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timezone_offset'), 'exclude': lambda f: f is None }})
    r"""Time zone UTC offset in seconds. Positive offset indicates east of UTC; negative offset indicates west of UTC; and null indicates the time zone information is unavailable at source."""
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""The reading type of the measurement. This is applicable only to Cholesterol, IGG and IGE."""
    

