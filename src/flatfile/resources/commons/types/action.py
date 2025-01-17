# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .action_mode import ActionMode
from .action_schedule import ActionSchedule


class Action(pydantic.BaseModel):
    slug: typing.Optional[str]
    operation: typing.Optional[str]
    mode: typing.Optional[ActionMode]
    label: str
    tooltip: typing.Optional[str]
    type: typing.Optional[str]
    description: typing.Optional[str]
    schedule: typing.Optional[ActionSchedule]
    primary: typing.Optional[bool]
    confirm: typing.Optional[bool]
    icon: typing.Optional[str]
    require_all_valid: typing.Optional[bool] = pydantic.Field(alias="requireAllValid")
    require_selection: typing.Optional[bool] = pydantic.Field(alias="requireSelection")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
