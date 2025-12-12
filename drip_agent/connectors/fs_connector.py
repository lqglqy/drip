from .base import BaseConnector
import os


class FSConnector(BaseConnector):
    def __init__(self, root_path: str):
        self.root_path = root_path

    def open(self):
        pass

    def close(self):
        pass

    def list(self, path: str):
        full = os.path.join(self.root_path, path)
        try:
            return os.listdir(full)
        except Exception:
            return []
