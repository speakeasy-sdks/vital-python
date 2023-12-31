"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .sleepv2indb import SleepV2InDB
from dataclasses_json import Undefined, dataclass_json
from typing import List
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RawSleep:
    sleep: List[SleepV2InDB] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sleep') }})
    

