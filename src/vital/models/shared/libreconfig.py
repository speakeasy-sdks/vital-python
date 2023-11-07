"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from vital import utils


@dataclasses.dataclass
class PracticeID:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LibreConfig:
    practice_id: PracticeID = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('practice_id') }})
    

