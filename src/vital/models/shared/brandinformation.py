"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class BrandInformation:
    brand_color: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('brand_color') }})
    company_address: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company_address') }})
    company_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company_name') }})
    company_website: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company_website') }})
    support_email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('support_email') }})
    
