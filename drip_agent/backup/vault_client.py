class VaultClient:
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    def upload(self, data, path: str):
        # TODO: implement S3/MinIO upload
        return {"uploaded": True, "path": path}
