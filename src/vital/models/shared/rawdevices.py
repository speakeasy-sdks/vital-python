"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import devicev2indb as shared_devicev2indb
from dataclasses_json import Undefined, dataclass_json
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class RawDevices:
    devices: list[shared_devicev2indb.DeviceV2InDB] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('devices') }})
    

