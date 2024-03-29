"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import teamindb as shared_teamindb
from ...models.shared import teamupdate as shared_teamupdate
from typing import Optional


@dataclasses.dataclass
class UpdateTeamV2TeamTeamIDPatchRequest:
    team_update: shared_teamupdate.TeamUpdate = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    team_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'team_id', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class UpdateTeamV2TeamTeamIDPatchResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    team_in_db: Optional[shared_teamindb.TeamInDB] = dataclasses.field(default=None)
    r"""Successful Response"""
    

