from abc import ABCMeta, abstractmethod


class PasswordHasher(metaclass=ABCMeta):
    @abstractmethod
    def hash(self, passwd: str) -> str:
        pass
