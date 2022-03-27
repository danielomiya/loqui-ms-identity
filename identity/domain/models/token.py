from dataclasses import dataclass


@dataclass
class Token:
    id_token: str
    token_type: str
    access_token: str
    refresh_token: str
    scope: str = "*"
    expires_in: int = 3600
