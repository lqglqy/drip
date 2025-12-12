import logging
from drip_agent.client.models import Job
from drip_agent.backup import backup_runner


def run(job: Job):
    logging.info("backup_executor running job=%s", job.id)
    res = backup_runner.run_backup(job.payload)
    logging.debug("backup result: %s", res)
    return res
