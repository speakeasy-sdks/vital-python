"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import consent as shared_consent
from ..shared import healthinsurancecreaterequest as shared_healthinsurancecreaterequest
from ..shared import patientaddresscompatible as shared_patientaddresscompatible
from ..shared import patientdetails as shared_patientdetails
from ..shared import physiciancreaterequest as shared_physiciancreaterequest
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateOrderRequestCompatible:
    r"""Schema for the create Order endpoint."""
    lab_test_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lab_test_id') }})
    patient_address: shared_patientaddresscompatible.PatientAddressCompatible = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('patient_address') }})
    patient_details: shared_patientdetails.PatientDetails = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('patient_details') }})
    user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_id') }})
    consents: Optional[list[shared_consent.Consent]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('consents'), 'exclude': lambda f: f is None }})
    health_insurance: Optional[shared_healthinsurancecreaterequest.HealthInsuranceCreateRequest] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('health_insurance'), 'exclude': lambda f: f is None }})
    physician: Optional[shared_physiciancreaterequest.PhysicianCreateRequest] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('physician'), 'exclude': lambda f: f is None }})
    priority: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('priority'), 'exclude': lambda f: f is None }})
    r"""Defines whether order is priority or not. Only available for Labcorp. For Labcorp, this corresponds to a STAT order."""
    

