"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import brandinformation as shared_brandinformation
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional
from vital import utils

class TeamCreatePhysicianNetworkT(str, Enum):
    r"""An enumeration."""
    WHEEL = 'WHEEL'
    OPENLOOP = 'OPENLOOP'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TeamCreate:
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    airtable_api_key: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airtable_api_key'), 'exclude': lambda f: f is None }})
    airtable_base_id: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airtable_base_id'), 'exclude': lambda f: f is None }})
    api_key: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key'), 'exclude': lambda f: f is None }})
    brand_information: Optional[shared_brandinformation.BrandInformation] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('brand_information'), 'exclude': lambda f: f is None }})
    client_id: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    client_secret: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret'), 'exclude': lambda f: f is None }})
    ff_apple_mobile_app_enabled: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ff_apple_mobile_app_enabled'), 'exclude': lambda f: f is None }})
    ff_wheel_enabled: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ff_wheel_enabled'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    lab_test_delegated_flow_enabled: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lab_test_delegated_flow_enabled'), 'exclude': lambda f: f is None }})
    lab_tests_patient_communication_enabled: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lab_tests_patient_communication_enabled'), 'exclude': lambda f: f is None }})
    lab_tests_patient_email_communication_enabled: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lab_tests_patient_email_communication_enabled'), 'exclude': lambda f: f is None }})
    lab_tests_patient_sms_communication_enabled: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lab_tests_patient_sms_communication_enabled'), 'exclude': lambda f: f is None }})
    message_templates_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message_templates_url'), 'exclude': lambda f: f is None }})
    physician_network: Optional[TeamCreatePhysicianNetworkT] = dataclasses.field(default=TeamCreatePhysicianNetworkT.OPENLOOP, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('physician_network'), 'exclude': lambda f: f is None }})
    subscription_status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subscription_status'), 'exclude': lambda f: f is None }})
    svix_app_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('svix_app_id'), 'exclude': lambda f: f is None }})
    webhook_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('webhook_secret'), 'exclude': lambda f: f is None }})
    
