"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PhlebotomyAreaInfo:
    is_served: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_served') }})
    

