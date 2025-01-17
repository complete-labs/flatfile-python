# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from ...commons.types.account_id import AccountId


class EventToken(pydantic.BaseModel):
    """
    Properties used to allow users to connect to the event bus
    """

    account_id: typing.Optional[AccountId] = pydantic.Field(alias="accountId")
    subscribe_key: typing.Optional[str] = pydantic.Field(
        alias="subscribeKey", description="The id of the event bus to subscribe to"
    )
    ttl: typing.Optional[float] = pydantic.Field(description="Time to live in minutes")
    token: typing.Optional[str]

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
