from dataclasses import dataclass
from typing import Optional

from starlette.responses import JSONResponse

from app.utils.common_methods import build_response


@dataclass
class ResultFromBL:
    success: bool
    message: Optional[str] = None
    data: Optional[dict] = None


class ResultFromHandler:
    """The responses from the controller have been separated because different behavior may appear
    in the future when processing specific responses, and also to improve the readability of the code."""

    @staticmethod
    def success(data: dict = None, message: str = None, status_code: int = 200):
        content = build_response(data=data, message=message)
        content['status'] = "success"

        return JSONResponse(
            status_code=status_code,
            content=content
        )

    @staticmethod
    def error(data: dict = None, message: str = None, status_code: int = 400):
        content = build_response(data=data, message=message)
        content['status'] = "error"

        return JSONResponse(
            status_code=status_code,
            content=content
        )



