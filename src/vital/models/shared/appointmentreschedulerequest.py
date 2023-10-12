"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AppointmentRescheduleRequest:
    r"""Pydantic BaseModel that supports `hidden` field property.

    A field with `hidden=True` will not be included in the schema (OpenAPI spec).
    """
    booking_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('booking_key') }})
    

