"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import labtestcollectionmethod as shared_labtestcollectionmethod
from ..shared import labtestsampletype as shared_labtestsampletype
from dataclasses_json import Undefined, dataclass_json
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ClientFacingLab:
    city: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('city') }})
    collection_methods: list[shared_labtestcollectionmethod.LabTestCollectionMethod] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collection_methods') }})
    first_line_address: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('first_line_address') }})
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    sample_types: list[shared_labtestsampletype.LabTestSampleType] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sample_types') }})
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug') }})
    zipcode: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('zipcode') }})
    
