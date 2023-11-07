"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .energy import Energy
from .macros import Macros
from .micros import Micros
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ClientFacingFood:
    energy: Optional[Energy] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('energy'), 'exclude': lambda f: f is None }})
    macros: Optional[Macros] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('macros'), 'exclude': lambda f: f is None }})
    micros: Optional[Micros] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('micros'), 'exclude': lambda f: f is None }})
    

