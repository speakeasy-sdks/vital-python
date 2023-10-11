"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import clientfacingsleepstream as shared_clientfacingsleepstream
from dataclasses_json import Undefined, dataclass_json
from datetime import date, datetime
from typing import Optional
from vital import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ClientFacingSleepSource:
    r"""Source summarizes where a sample or a summary is sourced from.
    At minimum, the source provider is always included.
    """
    logo: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logo') }})
    r"""Deprecated.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Deprecated.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    provider: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provider') }})
    r"""Provider slug. e.g., `oura`, `fitbit`, `garmin`."""
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug') }})
    r"""Deprecated.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    app_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('app_id'), 'exclude': lambda f: f is None }})
    r"""The identifier of the app which recorded this summary. This is only applicable to multi-source providers like Apple Health and Android Health Connect."""
    type: Optional[str] = dataclasses.field(default='unknown', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""The type of the data source (app or device) by which the summary or the timeseries data were recorded. This defaults to `unknown` when Vital cannot extract or infer that information"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ClientFacingSleep:
    awake: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('awake') }})
    r"""Total amount of awake time registered during the sleep period::seconds"""
    bedtime_start: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bedtime_start'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""UTC Time when the sleep period started"""
    bedtime_stop: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bedtime_stop'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""UTC Time when the sleep period ended"""
    calendar_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('calendar_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""Date of the sleep summary in the YYYY-mm-dd format. This generally matches the sleep end date."""
    date_: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""Date of the specified record, formatted as ISO8601 datetime string in UTC 00:00. Deprecated in favour of calendar_date.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    deep: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deep') }})
    r"""Total amount of deep (N3) sleep registered during the sleep period::seconds"""
    duration: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('duration') }})
    r"""Total duration of the sleep period (sleep.duration = sleep.bedtime_end - sleep.bedtime_start)::seconds"""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    light: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('light') }})
    r"""Total amount of light sleep registered during the sleep period::seconds"""
    rem: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rem') }})
    r"""Total amount of REM sleep registered during the sleep period, minutes::seconds"""
    source: ClientFacingSleepSource = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source') }})
    r"""Source the data has come from."""
    total: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total') }})
    r"""Total amount of sleep registered during the sleep period (sleep.total = sleep.rem + sleep.light + sleep.deep)::seconds"""
    user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_id') }})
    r"""User id returned by vital create user request. This id should be stored in your database against the user and used for all interactions with the vital api."""
    average_hrv: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('average_hrv'), 'exclude': lambda f: f is None }})
    r"""The average heart rate variability registered during the sleep period::rmssd"""
    efficiency: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('efficiency'), 'exclude': lambda f: f is None }})
    r"""Sleep efficiency is the percentage of the sleep period spent asleep (100% * sleep.total / sleep.duration)::perc"""
    hr_average: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hr_average'), 'exclude': lambda f: f is None }})
    r"""The average heart rate registered during the sleep period::beats per minute"""
    hr_lowest: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hr_lowest'), 'exclude': lambda f: f is None }})
    r"""The lowest heart rate (5 minutes sliding average) registered during the sleep period::beats per minute"""
    latency: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('latency'), 'exclude': lambda f: f is None }})
    r"""Detected latency from bedtime_start to the beginning of the first five minutes of persistent sleep::seconds"""
    respiratory_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('respiratory_rate'), 'exclude': lambda f: f is None }})
    r"""Average respiratory rate::breaths per minute"""
    score: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('score'), 'exclude': lambda f: f is None }})
    r"""A value between 1 and 100 representing how well the user slept. Currently only available for Withings, Oura, Whoop and Garmin::scalar"""
    skin_temperature: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('skin_temperature'), 'exclude': lambda f: f is None }})
    r"""The skin temperature::celcius"""
    sleep_stream: Optional[shared_clientfacingsleepstream.ClientFacingSleepStream] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sleep_stream'), 'exclude': lambda f: f is None }})
    temperature_delta: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('temperature_delta'), 'exclude': lambda f: f is None }})
    r"""Skin temperature deviation from the long-term temperature average::celcius"""
    timezone_offset: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timezone_offset'), 'exclude': lambda f: f is None }})
    r"""Timezone offset from UTC as seconds. For example, EEST (Eastern European Summer Time, +3h) is 10800. PST (Pacific Standard Time, -8h) is -28800::seconds"""
    

