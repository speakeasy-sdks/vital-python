"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class MacrosFats:
    r"""Details of fat content"""
    monounsaturated: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('monounsaturated'), 'exclude': lambda f: f is None }})
    r"""Amount of monounsaturated fats in grams (g)"""
    omega3: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('omega3'), 'exclude': lambda f: f is None }})
    r"""Amount of Omega-3 fatty acids in grams (g)"""
    omega6: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('omega6'), 'exclude': lambda f: f is None }})
    r"""Amount of Omega-6 fatty acids in grams (g)"""
    polyunsaturated: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('polyunsaturated'), 'exclude': lambda f: f is None }})
    r"""Amount of polyunsaturated fats in grams (g)"""
    saturated: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('saturated'), 'exclude': lambda f: f is None }})
    r"""Amount of saturated fats in grams (g)"""
    total: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total'), 'exclude': lambda f: f is None }})
    r"""Total amount of fats in grams (g)"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Macros:
    alcohol: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('alcohol'), 'exclude': lambda f: f is None }})
    r"""Amount of alcohol in grams (g)"""
    carbs: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('carbs'), 'exclude': lambda f: f is None }})
    r"""Amount of carbohydrates in grams (g)"""
    fats: Optional[MacrosFats] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fats'), 'exclude': lambda f: f is None }})
    r"""Details of fat content"""
    fibre: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fibre'), 'exclude': lambda f: f is None }})
    r"""Amount of dietary fiber in grams (g)"""
    protein: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('protein'), 'exclude': lambda f: f is None }})
    r"""Amount of protein in grams (g)"""
    sugar: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sugar'), 'exclude': lambda f: f is None }})
    r"""Amount of sugar in grams (g)"""
    water: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('water'), 'exclude': lambda f: f is None }})
    r"""Amount of water in grams (g)"""
    

