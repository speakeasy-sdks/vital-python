"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UserRefreshErrorResponse(Exception):
    error: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    success: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('success') }})
    r"""Whether operation was successful or not"""
    user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_id') }})
    r"""A unique ID representing the end user. Typically this will be a user ID from your application. Personally identifiable information, such as an email address or phone number, should not be used in the client_user_id."""
    failed_sources: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failed_sources'), 'exclude': lambda f: f is None }})
    

    def __str__(self) -> str:
        return utils.marshal_json(self, type(self))
