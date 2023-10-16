"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import libreconfig as shared_libreconfig
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TeamConfig:
    libreview: shared_libreconfig.LibreConfig = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('libreview') }})
    texts_enabled: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('texts_enabled'), 'exclude': lambda f: f is None }})
    
