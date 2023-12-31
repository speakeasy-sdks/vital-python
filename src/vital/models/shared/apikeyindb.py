"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .apikeyrole import APIKeyRole
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from typing import Optional
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class APIKeyInDB:
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    in_app: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('in_app') }})
    label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('label') }})
    role: APIKeyRole = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('role') }})
    r"""An enumeration."""
    team_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('team_id') }})
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    deleted_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deleted_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    

