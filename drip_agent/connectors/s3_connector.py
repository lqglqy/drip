from .base import BaseConnector


class S3Connector(BaseConnector):
    def __init__(self, bucket: str, **kwargs):
        self.bucket = bucket

    def open(self):
        pass

    def close(self):
        pass

    def list(self, path: str):
        return []
