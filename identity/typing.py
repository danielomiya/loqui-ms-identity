from typing import Any, Dict, Tuple, TypeVar

T = TypeVar("T")
F = TypeVar("F")
JSON = Dict[str, Any]
HTTPStatus = int
Response = Tuple[JSON, HTTPStatus]
