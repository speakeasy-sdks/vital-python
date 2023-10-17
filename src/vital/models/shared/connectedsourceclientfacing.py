"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConnectedSourceClientFacingProvider:
    r"""A vendor, a service, or a platform which Vital can connect with."""
    logo: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logo') }})
    r"""URL for source logo"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Name of source of information"""
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug') }})
    r"""Slug for designated source"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConnectedSourceClientFacing:
    created_on: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_on'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""When your item is created"""
    provider: ConnectedSourceClientFacingProvider = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provider') }})
    r"""The provider of this connected source."""
    source: ConnectedSourceClientFacingProvider = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source') }})
    r"""Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible."""
    

