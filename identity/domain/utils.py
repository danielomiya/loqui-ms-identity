from datetime import datetime, timedelta
from typing import Callable, Type, Union

from identity.typing import F, T


def parse_iso_datetime(value: str) -> datetime:
    dttm_part, _, us = value.partition(".")
    dttm_part = datetime.strptime(dttm_part, "%Y-%m-%dT%H:%M:%S")
    us = int(us.rstrip("Z"), 10)
    return dttm_part + timedelta(microseconds=us)


def get_or_init(cls: Union[T, Type[T]]) -> T:
    if isinstance(cls, type):
        return cls()
    return cls


def make_getter(o: T) -> Callable[[str], F]:
    if hasattr(o, "__getitem__"):  # if it's dict-like
        return o.__getitem__

    # or maybe dataclass
    return lambda name: getattr(o, name, None)
