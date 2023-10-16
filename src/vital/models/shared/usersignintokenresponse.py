"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import usersignintoken as shared_usersignintoken
from dataclasses_json import Undefined, dataclass_json
from typing import Union
from vital import utils



@dataclasses.dataclass
class UserSignInTokenResponseSignInToken:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UserSignInTokenResponse:
    sign_in_token: Union[shared_usersignintoken.UserSignInToken, str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sign_in_token') }})
    user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_id') }})
    
