"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ClientFacingUserKey:
    client_user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_user_id') }})
    r"""A unique ID representing the end user. Typically this will be a user ID from your application. Personally identifiable information, such as an email address or phone number, should not be used in the client_user_id."""
    user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_id') }})
    r"""User id returned by vital create user request. This id should be stored in your database against the user and used for all interactions with the vital api."""
    

