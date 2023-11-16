"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .clientfacingapikey import ClientFacingAPIKey
from .teamconfig import TeamConfig
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ClientFacingTeam:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    lab_tests_patient_communication_enabled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lab_tests_patient_communication_enabled') }})
    lab_tests_patient_email_communication_enabled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lab_tests_patient_email_communication_enabled') }})
    lab_tests_patient_sms_communication_enabled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lab_tests_patient_sms_communication_enabled') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    testkits_texts_enabled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('testkits_texts_enabled') }})
    r"""Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible."""
    airtable_api_key: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airtable_api_key'), 'exclude': lambda f: f is None }})
    airtable_base_id: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airtable_base_id'), 'exclude': lambda f: f is None }})
    api_key: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key'), 'exclude': lambda f: f is None }})
    api_keys: Optional[List[ClientFacingAPIKey]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_keys'), 'exclude': lambda f: f is None }})
    client_id: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    client_secret: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret'), 'exclude': lambda f: f is None }})
    configuration: Optional[TeamConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('configuration'), 'exclude': lambda f: f is None }})
    logo_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logo_url'), 'exclude': lambda f: f is None }})
    svix_app_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('svix_app_id'), 'exclude': lambda f: f is None }})
    webhook_secret: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('webhook_secret'), 'exclude': lambda f: f is None }})
    

