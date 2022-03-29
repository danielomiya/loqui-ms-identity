from datetime import datetime
from typing import Any

from flask.json import JSONEncoder


class JSONSerializer(JSONEncoder):
    def default(self, o: Any) -> str:
        if isinstance(o, datetime):
            if o.utcoffset() is not None:
                o = o - o.utcoffset()
            return o.isoformat("T")

        raise TypeError(f"unknown type {o.__class__.__name__}")
