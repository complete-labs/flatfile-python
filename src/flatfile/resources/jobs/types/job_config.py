# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from ...commons.types.file_id import FileId
from .job_destination import JobDestination
from .job_mode import JobMode
from .job_source import JobSource
from .job_status import JobStatus
from .job_subject import JobSubject
from .job_type import JobType
from .job_update_config import JobUpdateConfig
from .trigger import Trigger


class JobConfig(pydantic.BaseModel):
    """
    A single unit of work that a pipeline will execute
    """

    type: JobType = pydantic.Field(description="The type of job")
    operation: str = pydantic.Field(description='the type of operation to perform on the data. For example, "export".')
    source: JobSource
    destination: typing.Optional[JobDestination]
    config: typing.Optional[JobUpdateConfig]
    trigger: typing.Optional[Trigger] = pydantic.Field(description="the type of trigger to use for this job")
    status: typing.Optional[JobStatus] = pydantic.Field(description="the status of the job")
    progress: typing.Optional[float] = pydantic.Field(description="the progress of the job")
    file_id: typing.Optional[FileId] = pydantic.Field(alias="fileId")
    mode: typing.Optional[JobMode] = pydantic.Field(description="the mode of the job")
    input: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        description="Input parameters for this job type."
    )
    subject: typing.Optional[JobSubject] = pydantic.Field(description="Subject parameters for this job type.")
    outcome: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(description="Outcome summary of job.")
    info: typing.Optional[str] = pydantic.Field(description="Current status of job in text")
    managed: typing.Optional[bool] = pydantic.Field(
        description="Indicates if Flatfile is managing the control flow of this job or if it is being manually tracked."
    )

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