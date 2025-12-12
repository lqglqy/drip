import logging


def run_backup(payload: dict):
    # Minimal placeholder: payload contains 'source' and 'destination'
    logging.info("run_backup payload=%s", payload)
    # Pretend we uploaded to a vault and return metadata
    return {"status": "OK", "location": payload.get("destination")}
