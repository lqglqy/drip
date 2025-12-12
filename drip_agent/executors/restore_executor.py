import logging
from drip_agent.client.models import Job


def run(job: Job):
    logging.info("restore_executor running job=%s", job.id)
    # TODO: implement restore flow
    logging.warning("restore_executor is a stub")
    return {"status": "NOT_IMPLEMENTED"}
