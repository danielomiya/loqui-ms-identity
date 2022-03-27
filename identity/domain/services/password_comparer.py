from abc import ABCMeta, abstractmethod


class PasswordComparer(metaclass=ABCMeta):
    @abstractmethod
    def compare(self, passwd: str, hashed: str) -> bool:
        pass
