import bcrypt
from identity.domain.services.password_comparer import PasswordComparer
from identity.domain.services.password_hasher import PasswordHasher


ENCODING = "utf8"


class BcryptService(PasswordComparer, PasswordHasher):
    def hash(self, passwd: str) -> str:
        return bcrypt.hashpw(passwd.encode(ENCODING), bcrypt.gensalt()).decode(ENCODING)

    def compare(self, passwd: str, hashed: str) -> bool:
        return bcrypt.checkpw(passwd.encode(ENCODING), hashed.encode(ENCODING))
