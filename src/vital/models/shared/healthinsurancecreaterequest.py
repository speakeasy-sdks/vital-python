"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import address as shared_address
from ..shared import jpeg as shared_jpeg
from ..shared import png as shared_png
from ..shared import responsiblerelationship as shared_responsiblerelationship
from dataclasses_json import Undefined, dataclass_json
from typing import Optional, Union
from vital import utils



@dataclasses.dataclass
class HealthInsuranceCreateRequestBackImage:
    pass



@dataclasses.dataclass
class HealthInsuranceCreateRequestFrontImage:
    pass



@dataclasses.dataclass
class HealthInsuranceCreateRequestPatientSignatureImage:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class HealthInsuranceCreateRequestPersonDetails:
    r"""Responsible details when the value of responsible_relationship is not 'Self'."""
    address: shared_address.Address = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address') }})
    first_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('first_name') }})
    last_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_name') }})
    phone_number: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone_number') }})
    phone_type: Optional[str] = dataclasses.field(default='Mobile', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone_type'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class HealthInsuranceCreateRequest:
    assessment_plan: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assessment_plan'), 'exclude': lambda f: f is None }})
    r"""Textual description of what are the physician assessments and testing plans."""
    back_image: Optional[Union[shared_jpeg.Jpeg, shared_png.Png]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('back_image'), 'exclude': lambda f: f is None }})
    r"""An image of the back of the patient insurance card."""
    diagnosis_codes: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('diagnosis_codes'), 'exclude': lambda f: f is None }})
    r"""Diagnosis codes for insurance billing."""
    front_image: Optional[Union[shared_jpeg.Jpeg, shared_png.Png]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('front_image'), 'exclude': lambda f: f is None }})
    r"""An image of the front of the patient insurance card."""
    insurance_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('insurance_id'), 'exclude': lambda f: f is None }})
    r"""Insurance unique number assigned to a patient, usually present on the insurance card."""
    patient_signature_image: Optional[Union[shared_jpeg.Jpeg, shared_png.Png]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('patient_signature_image'), 'exclude': lambda f: f is None }})
    r"""An image of the patient signature for health insurance billing."""
    payor_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payor_code'), 'exclude': lambda f: f is None }})
    r"""Unique identifier representing a specific Health Insurance."""
    responsible_details: Optional[HealthInsuranceCreateRequestPersonDetails] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('responsible_details'), 'exclude': lambda f: f is None }})
    r"""Responsible details when the value of responsible_relationship is not 'Self'."""
    responsible_relationship: Optional[shared_responsiblerelationship.ResponsibleRelationship] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('responsible_relationship'), 'exclude': lambda f: f is None }})
    r"""Relationship between the patient and the insurance contractor. Values can be (Self, Spouse, Other Relationship)."""
    subjective: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subjective'), 'exclude': lambda f: f is None }})
    r"""Textual description of what are the patient symptoms and attempted treatments."""
    
