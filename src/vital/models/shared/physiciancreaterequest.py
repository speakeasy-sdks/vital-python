"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .jpeg import Jpeg
from .png import Png
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional, Union
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PhysicianCreateRequest:
    first_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('first_name') }})
    last_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_name') }})
    npi: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('npi') }})
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    licensed_states: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('licensed_states'), 'exclude': lambda f: f is None }})
    signature_image: Optional[Union[Jpeg, Png]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('signature_image'), 'exclude': lambda f: f is None }})
    r"""An image of the physician signature for health insurance billing"""
    

