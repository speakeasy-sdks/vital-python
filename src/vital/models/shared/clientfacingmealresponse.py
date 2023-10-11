"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import mealindbbase_clientfacingsource_ as shared_mealindbbase_clientfacingsource_
from dataclasses_json import Undefined, dataclass_json
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ClientFacingMealResponse:
    meals: list[shared_mealindbbase_clientfacingsource_.MealInDBBaseClientFacingSource] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('meals') }})
    

