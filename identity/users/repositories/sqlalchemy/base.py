import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


class SQLAlchemyMixin:
    def __init__(self, url: str = os.getenv("LOQUI_IDENTITIY_DB_URL")):
        self.engine = create_engine(url)
        self.session_maker = sessionmaker(bind=self.engine)

    def get_conn(self):
        return self.engine.connect()

    def get_session(self) -> Session:
        return self.session_maker()
