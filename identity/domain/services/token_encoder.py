from abc import ABCMeta, abstractmethod
from typing import Any, Dict


class TokenEncoder(metaclass=ABCMeta):
    """
    Encoder of tokens
    """

    @abstractmethod
    def encode(self, claims: Dict[str, Any]) -> str:
        """
        Encodes a dictionary of claims to a signable token

        Args:
            claims (Dict[str, Any]): user claims

        Returns:
            str: serialized token
        """
