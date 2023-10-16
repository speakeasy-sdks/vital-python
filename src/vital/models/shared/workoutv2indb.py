"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import clientfacingprovider as shared_clientfacingprovider
from ..shared import clientfacingsport as shared_clientfacingsport
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from typing import Optional
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class WorkoutV2InDB:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    provider_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provider_id') }})
    source: shared_clientfacingprovider.ClientFacingProvider = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source') }})
    r"""A vendor, a service, or a platform which Vital can connect with."""
    source_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source_id') }})
    sport: shared_clientfacingsport.ClientFacingSport = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sport') }})
    sport_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sport_id') }})
    timestamp: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timestamp'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_id') }})
    data: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    priority_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('priority_id'), 'exclude': lambda f: f is None }})
    
