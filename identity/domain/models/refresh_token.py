from dataclasses import dataclass
from datetime import datetime


@dataclass
class RefreshToken:
    id: str
    access_token_id: str
    is_revoked: bool
    expires_at: datetime
