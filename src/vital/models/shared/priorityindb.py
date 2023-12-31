"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PriorityInDB:
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    priority: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('priority') }})
    source_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source_id') }})
    team_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('team_id') }})
    data_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data_type'), 'exclude': lambda f: f is None }})
    

