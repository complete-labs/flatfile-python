# This file was auto-generated by Fern from our API Definition.

from ....core.api_error import ApiError
from ..types.errors import Errors


class BadRequestError(ApiError):
    def __init__(self, body: Errors):
        super().__init__(status_code=400, body=body)