from .base import BaseConnector


class SnowflakeConnector(BaseConnector):
    def __init__(self, account: str, user: str, password: str):
        self.account = account

    def open(self):
        pass

    def close(self):
        pass

    def list(self, path: str):
        return []
