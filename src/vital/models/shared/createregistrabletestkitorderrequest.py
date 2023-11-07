"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .shippingaddress import ShippingAddress
from dataclasses_json import Undefined, dataclass_json
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateRegistrableTestkitOrderRequest:
    lab_test_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lab_test_id') }})
    shipping_details: ShippingAddress = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shipping_details') }})
    user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_id') }})
    

