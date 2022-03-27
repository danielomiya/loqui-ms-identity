import bcrypt
from identity.domain.services.password_comparer import PasswordComparer
from identity.domain.services.password_hasher import PasswordHasher


class BcryptService(PasswordComparer, PasswordHasher):
    def hash(self, passwd: str) -> str:
        return bcrypt.hashpw(passwd.encode("utf8"), bcrypt.gensalt()).decode("utf8")

    def compare(self, passwd: str, hashed: str) -> bool:
        return bcrypt.checkpw(passwd, hashed)
