"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import clientfacingteam as shared_clientfacingteam
from typing import Optional


@dataclasses.dataclass
class GetTeamV2TeamTeamIDGetRequest:
    team_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'team_id', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetTeamV2TeamTeamIDGetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    client_facing_team: Optional[shared_clientfacingteam.ClientFacingTeam] = dataclasses.field(default=None)
    r"""Successful Response"""
    

