# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class Compiler(str, enum.Enum):
    """
    The compiler of the agent
    """

    JS = "js"

    def visit(self, js: typing.Callable[[], T_Result]) -> T_Result:
        if self is Compiler.JS:
            return js()