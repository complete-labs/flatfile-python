# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from ...commons.types.event_id import EventId
from .base_event import BaseEvent


class GenericEvent(BaseEvent):
    id: EventId
    created_at: dt.datetime = pydantic.Field(alias="createdAt", description="Date the event was created")
    deleted_at: typing.Optional[dt.datetime] = pydantic.Field(
        alias="deletedAt", description="Date the event was deleted"
    )
    acknowledged_at: typing.Optional[dt.datetime] = pydantic.Field(
        alias="acknowledgedAt", description="Date the event was acknowledged"
    )
    acknowledged_by: typing.Optional[str] = pydantic.Field(
        alias="acknowledgedBy", description="The actor (user or system) who acknowledged the event"
    )
    payload: typing.Dict[str, typing.Any]

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
