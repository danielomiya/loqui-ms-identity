from abc import ABCMeta, abstractmethod
from typing import Any, Dict


class TokenDecoder(metaclass=ABCMeta):
    """
    Decoder of tokens
    """

    @abstractmethod
    def decode(self, token: str) -> Dict[str, Any]:
        """
        Decodes a token to a dictionary of claims

        Args:
            token (str): input token

        Returns:
            Dict[str, Any]: claims
        """
