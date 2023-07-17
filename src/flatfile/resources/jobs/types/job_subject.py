# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .collection_job_subject import CollectionJobSubject
from .resource_job_subject import ResourceJobSubject


class JobSubject_Resource(ResourceJobSubject):
    type: typing_extensions.Literal["resource"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


class JobSubject_Collection(CollectionJobSubject):
    type: typing_extensions.Literal["collection"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


JobSubject = typing.Union[JobSubject_Resource, JobSubject_Collection]