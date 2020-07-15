from dataclasses import dataclass
from datetime import datetime
from typing import Any

@dataclass
class ExceptionResponse:
    message: str
    status: int
    date: Any = datetime.now()
