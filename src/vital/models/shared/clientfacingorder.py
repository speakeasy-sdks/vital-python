"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .clientfacingathomephlebotomyorderdetails import ClientFacingAtHomePhlebotomyOrderDetails
from .clientfacinglab import ClientFacingLab
from .clientfacingmarker import ClientFacingMarker
from .clientfacingorderevent import ClientFacingOrderEvent
from .clientfacingtestkitorderdetails import ClientFacingTestKitOrderDetails
from .clientfacingwalkinorderdetails import ClientFacingWalkInOrderDetails
from .labtestcollectionmethod import LabTestCollectionMethod
from .labtestsampletype import LabTestSampleType
from .ordertoplevelstatus import OrderTopLevelStatus
from .physicianclientfacing import PhysicianClientFacing
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from typing import List, Optional, Union
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ClientFacingOrderClientFacingLabTest:
    r"""The Vital Test associated with the order"""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    is_active: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_active') }})
    method: LabTestCollectionMethod = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    r"""The method used to perform a lab test."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    price: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('price') }})
    sample_type: LabTestSampleType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sample_type') }})
    r"""The type of sample used to perform a lab test."""
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug') }})
    fasting: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fasting'), 'exclude': lambda f: f is None }})
    r"""Defines whether a lab test requires fasting. Only available for Labcorp."""
    is_delegated: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_delegated'), 'exclude': lambda f: f is None }})
    r"""Denotes whether a lab test requires using non-Vital physician networks. If it does then it's delegated - no otherwise."""
    lab: Optional[ClientFacingLab] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lab'), 'exclude': lambda f: f is None }})
    markers: Optional[List[ClientFacingMarker]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('markers'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ClientFacingOrderPatientAddressCompatible:
    r"""Patient Address"""
    city: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('city') }})
    country: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country') }})
    state: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state') }})
    street: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street') }})
    zip: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('zip') }})
    phone_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone_number'), 'exclude': lambda f: f is None }})
    receiver_name: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('receiver_name'), 'exclude': lambda f: f is None }})
    street_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street_number'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ClientFacingPatientDetailsCompatible:
    r"""Patient Details"""
    dob: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dob'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    gender: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gender') }})
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    first_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('first_name'), 'exclude': lambda f: f is None }})
    last_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_name'), 'exclude': lambda f: f is None }})
    phone_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone_number'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ClientFacingOrderShippingAddress:
    r"""Shipping Details. For unregistered testkit orders."""
    city: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('city') }})
    country: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country') }})
    first_line: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('first_line') }})
    phone_number: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone_number') }})
    receiver_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('receiver_name') }})
    state: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state') }})
    zip: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('zip') }})
    second_line: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('second_line'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ClientFacingOrder:
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""When your order was created"""
    details: Union[ClientFacingWalkInOrderDetails, ClientFacingTestKitOrderDetails, ClientFacingAtHomePhlebotomyOrderDetails] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details') }})
    events: List[ClientFacingOrderEvent] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('events') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The Vital Order ID"""
    lab_test: ClientFacingOrderClientFacingLabTest = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lab_test') }})
    r"""The Vital Test associated with the order"""
    team_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('team_id') }})
    r"""Your team id."""
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""When your order was last updated."""
    user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_id') }})
    r"""User id returned by vital create user request. This id should be stored in your database against the user and used for all interactions with the vital api."""
    health_insurance_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('health_insurance_id'), 'exclude': lambda f: f is None }})
    r"""Vital ID of the health insurance."""
    notes: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('notes'), 'exclude': lambda f: f is None }})
    r"""Notes associated with the order"""
    patient_address: Optional[ClientFacingOrderPatientAddressCompatible] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('patient_address'), 'exclude': lambda f: f is None }})
    r"""Patient Address"""
    patient_details: Optional[ClientFacingPatientDetailsCompatible] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('patient_details'), 'exclude': lambda f: f is None }})
    r"""Patient Details"""
    physician: Optional[PhysicianClientFacing] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('physician'), 'exclude': lambda f: f is None }})
    priority: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('priority'), 'exclude': lambda f: f is None }})
    r"""Defines whether order is priority or not. Only available for Labcorp. For Labcorp, this corresponds to a STAT order."""
    requisition_form_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requisition_form_url'), 'exclude': lambda f: f is None }})
    r"""DEPRECATED. Requistion form url."""
    sample_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sample_id'), 'exclude': lambda f: f is None }})
    r"""Sample ID"""
    shipping_details: Optional[ClientFacingOrderShippingAddress] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shipping_details'), 'exclude': lambda f: f is None }})
    r"""Shipping Details. For unregistered testkit orders."""
    status: Optional[OrderTopLevelStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""An enumeration."""
    

