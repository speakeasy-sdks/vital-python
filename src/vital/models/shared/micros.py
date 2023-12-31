"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import Dict, Optional
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Micros:
    minerals: Optional[Dict[str, float]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minerals'), 'exclude': lambda f: f is None }})
    r"""Amount of each mineral in grams (g)"""
    trace_elements: Optional[Dict[str, float]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trace_elements'), 'exclude': lambda f: f is None }})
    r"""Amount of each trace element in grams (g)"""
    vitamins: Optional[Dict[str, float]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vitamins'), 'exclude': lambda f: f is None }})
    r"""Amount of each vitamin in grams (g)"""
    

