# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .category_mapping import CategoryMapping


class EnumDetails(pydantic.BaseModel):
    """
    Only available if one or more of the destination fields is of type enum. Provides category mapping.
    """

    mapping: typing.Optional[typing.List[CategoryMapping]]
    unused_source_values: typing.Optional[typing.List[str]] = pydantic.Field(alias="unusedSourceValues")
    unused_destination_values: typing.Optional[typing.List[str]] = pydantic.Field(alias="unusedDestinationValues")

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