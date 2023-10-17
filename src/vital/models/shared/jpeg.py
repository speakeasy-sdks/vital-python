"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from vital import utils

class JpegContentType(str, Enum):
    IMAGE_JPEG = 'image/jpeg'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Jpeg:
    r"""An image of the back of the patient insurance card."""
    content: bytes = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content') }})
    content_type: JpegContentType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content_type') }})
    

