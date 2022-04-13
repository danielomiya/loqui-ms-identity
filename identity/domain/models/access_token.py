from dataclasses import dataclass
from datetime import datetime


@dataclass
class AccessToken:
    id: str
    user_id: int
    client_id: int
    scopes: str
    is_revoked: bool
    expires_at: datetime
    created_at: datetime
    updated_at: datetime
