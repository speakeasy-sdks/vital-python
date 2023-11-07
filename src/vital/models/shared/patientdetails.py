"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .gender import Gender
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatientDetails:
    dob: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dob'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    first_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('first_name') }})
    gender: Gender = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gender') }})
    r"""An enumeration."""
    last_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_name') }})
    phone_number: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone_number') }})
    

