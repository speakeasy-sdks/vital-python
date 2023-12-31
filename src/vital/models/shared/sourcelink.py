"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional
from vital import utils

class SourceLinkSourceAuthType(str, Enum):
    r"""An enumeration."""
    OAUTH = 'oauth'
    TEAM_OAUTH = 'team_oauth'
    SDK = 'sdk'
    PASSWORD = 'password'
    EMAIL = 'email'
    APP = 'app'
    UNKNOWN = ''


@dataclasses.dataclass
class FormComponents:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceLink:
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    logo: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logo') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug') }})
    auth_type: Optional[SourceLinkSourceAuthType] = dataclasses.field(default=SourceLinkSourceAuthType.OAUTH, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    form_components: Optional[FormComponents] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('form_components'), 'exclude': lambda f: f is None }})
    oauth_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('oauth_url'), 'exclude': lambda f: f is None }})
    

