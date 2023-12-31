"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LabResultsMetadata:
    age: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('age') }})
    date_reported: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date_reported') }})
    dob: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dob') }})
    patient: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('patient') }})
    specimen_number: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('specimen_number') }})
    clia_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clia_#'), 'exclude': lambda f: f is None }})
    date_collected: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date_collected'), 'exclude': lambda f: f is None }})
    date_received: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date_received'), 'exclude': lambda f: f is None }})
    interpretation: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('interpretation'), 'exclude': lambda f: f is None }})
    laboratory: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('laboratory'), 'exclude': lambda f: f is None }})
    provider: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provider'), 'exclude': lambda f: f is None }})
    status: Optional[str] = dataclasses.field(default='final', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    

