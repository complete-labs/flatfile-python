# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class Domain(str, enum.Enum):
    """
    The domain of the event
    """

    FILE = "file"
    SPACE = "space"
    WORKBOOK = "workbook"
    JOB = "job"
    DOCUMENT = "document"
    SHEET = "sheet"

    def visit(
        self,
        file: typing.Callable[[], T_Result],
        space: typing.Callable[[], T_Result],
        workbook: typing.Callable[[], T_Result],
        job: typing.Callable[[], T_Result],
        document: typing.Callable[[], T_Result],
        sheet: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Domain.FILE:
            return file()
        if self is Domain.SPACE:
            return space()
        if self is Domain.WORKBOOK:
            return workbook()
        if self is Domain.JOB:
            return job()
        if self is Domain.DOCUMENT:
            return document()
        if self is Domain.SHEET:
            return sheet()
