"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .bodyv2indb import BodyV2InDB
from dataclasses_json import Undefined, dataclass_json
from typing import List
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RawBody:
    body: List[BodyV2InDB] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('body') }})
    

