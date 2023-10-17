"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ClientFacingStream:
    altitude: Optional[List[float]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('altitude'), 'exclude': lambda f: f is None }})
    r"""Data points for altitude"""
    cadence: Optional[List[float]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cadence'), 'exclude': lambda f: f is None }})
    r"""RPM for cycling, Steps per minute for running"""
    distance: Optional[List[float]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('distance'), 'exclude': lambda f: f is None }})
    r"""Cumulated distance for exercise"""
    heartrate: Optional[List[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('heartrate'), 'exclude': lambda f: f is None }})
    r"""Heart rate in bpm"""
    lat: Optional[List[float]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lat'), 'exclude': lambda f: f is None }})
    r"""Latitude for data point"""
    lng: Optional[List[float]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lng'), 'exclude': lambda f: f is None }})
    r"""Longitude for data point"""
    power: Optional[List[float]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('power'), 'exclude': lambda f: f is None }})
    r"""Power in watts"""
    resistance: Optional[List[float]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resistance'), 'exclude': lambda f: f is None }})
    r"""Resistance on bike"""
    time: Optional[List[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('time'), 'exclude': lambda f: f is None }})
    r"""Corresponding time stamp in unix time for datapoint"""
    velocity_smooth: Optional[List[float]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('velocity_smooth'), 'exclude': lambda f: f is None }})
    r"""Velocity in m/s"""
    

