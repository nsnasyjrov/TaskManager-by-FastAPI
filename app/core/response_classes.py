from dataclasses import dataclass
from typing import Optional


@dataclass
class ResultFromBL:
    success: bool
    message: Optional[str] = None
    data: Optional[dict] = None