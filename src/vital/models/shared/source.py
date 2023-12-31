"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional
from vital import utils

class SourceSourceAuthType(str, Enum):
    r"""An enumeration."""
    OAUTH = 'oauth'
    TEAM_OAUTH = 'team_oauth'
    SDK = 'sdk'
    PASSWORD = 'password'
    EMAIL = 'email'
    APP = 'app'
    UNKNOWN = ''

class SourceType(str, Enum):
    r"""An enumeration."""
    APP = 'app'
    BLE = 'ble'
    DEVICE = 'device'
    LAB = 'lab'
    PROVIDER = 'provider'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Source:
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    logo: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logo') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug') }})
    auth_type: Optional[SourceSourceAuthType] = dataclasses.field(default=SourceSourceAuthType.OAUTH, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    backfill_num_days: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('backfill_num_days'), 'exclude': lambda f: f is None }})
    group: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('group'), 'exclude': lambda f: f is None }})
    is_active: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_active'), 'exclude': lambda f: f is None }})
    oauth_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('oauth_url'), 'exclude': lambda f: f is None }})
    source_type: Optional[SourceType] = dataclasses.field(default=SourceType.DEVICE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source_type'), 'exclude': lambda f: f is None }})
    

