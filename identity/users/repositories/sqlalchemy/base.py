import os

from sqlalchemy import create_engine


class SQLAlchemyMixin:
    def __init__(self, url: str = os.getenv("LOQUI_IDENTITIY_DB_URL")):
        self.engine = create_engine(url)

    def get_conn(self):
        return self.engine.connect()
