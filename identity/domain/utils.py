from datetime import datetime, timedelta


def parse_iso_datetime(value: str) -> datetime:
    dttm_part, _, us = value.partition(".")
    dttm_part = datetime.strptime(dttm_part, "%Y-%m-%dT%H:%M:%S")
    us = int(us.rstrip("Z"), 10)
    return dttm_part + timedelta(microseconds=us)
