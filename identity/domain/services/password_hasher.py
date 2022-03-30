from abc import ABCMeta, abstractmethod


class PasswordHasher(metaclass=ABCMeta):
    """
    Contract to implement password hashers
    """

    @abstractmethod
    def hash(self, passwd: str) -> str:
        """
        Hashes a password

        Args:
            passwd (str): password to hash

        Returns:
            str: returns a hash
        """
        raise NotImplementedError("override me")
