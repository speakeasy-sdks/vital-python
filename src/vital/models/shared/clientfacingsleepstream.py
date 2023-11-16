"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .clientfacingheartratetimeseries import ClientFacingHeartRateTimeseries
from .clientfacinghrvtimeseries import ClientFacingHRVTimeseries
from .clientfacinghypnogramtimeseries import ClientFacingHypnogramTimeseries
from .clientfacingrespiratoryratetimeseries import ClientFacingRespiratoryRateTimeseries
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ClientFacingSleepStream:
    heartrate: Optional[List[ClientFacingHeartRateTimeseries]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('heartrate'), 'exclude': lambda f: f is None }})
    hrv: Optional[List[ClientFacingHRVTimeseries]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hrv'), 'exclude': lambda f: f is None }})
    hypnogram: Optional[List[ClientFacingHypnogramTimeseries]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hypnogram'), 'exclude': lambda f: f is None }})
    respiratory_rate: Optional[List[ClientFacingRespiratoryRateTimeseries]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('respiratory_rate'), 'exclude': lambda f: f is None }})
    

