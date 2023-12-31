"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ShippingAddress:
    city: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('city') }})
    country: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country') }})
    first_line: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('first_line') }})
    phone_number: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone_number') }})
    receiver_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('receiver_name') }})
    state: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state') }})
    zip: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('zip') }})
    second_line: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('second_line'), 'exclude': lambda f: f is None }})
    

