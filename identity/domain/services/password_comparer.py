from abc import ABCMeta, abstractmethod


class PasswordComparer(metaclass=ABCMeta):
    """
    Contract to implement password comparison
    """

    @abstractmethod
    def compare(self, passwd: str, hashed: str) -> bool:
        """
        Compares two passwords

        Args:
            passwd (str): password to compare
            hashed (str): previous hash to compare

        Returns:
            bool: whether the password is equal
        """
        raise NotImplementedError("override me")
