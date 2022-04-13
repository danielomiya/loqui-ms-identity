from dataclasses import dataclass
from datetime import datetime


@dataclass
class Client:
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
