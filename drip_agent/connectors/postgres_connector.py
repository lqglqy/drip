from .base import BaseConnector


class PostgresConnector(BaseConnector):
    def __init__(self, dsn: str):
        self.dsn = dsn

    def open(self):
        pass

    def close(self):
        pass

    def list(self, path: str):
        # 'path' can be used to indicate table/schema
        return []
