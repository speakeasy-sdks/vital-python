"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OrgAddress:
    r"""Insurance business address returned for the insurance information required by Labcorp."""
    city: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('city') }})
    country: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country') }})
    first_line: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('first_line') }})
    state: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state') }})
    zip: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('zip') }})
    second_line: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('second_line'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ClientFacingPayorSearchResponse:
    code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code') }})
    r"""Payor code returned for the insurance information required by Labcorp."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Insurance name returned for the insurance information required by Labcorp."""
    org_address: OrgAddress = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org_address') }})
    r"""Insurance business address returned for the insurance information required by Labcorp."""
    

