import time
import logging
from drip_agent.client.control_plane_client import ControlPlaneClient
from drip_agent.client.models import Job
from drip_agent.executors import scan_executor, backup_executor, restore_executor


DEFAULT_POLL_INTERVAL = 5


def run(agent_id: str, client: ControlPlaneClient, poll_interval: int = DEFAULT_POLL_INTERVAL):
    logging.info("worker_loop started (agent=%s) poll_interval=%s", agent_id, poll_interval)
    while True:
        try:
            jobs = client.pull_jobs(agent_id)
            for job in jobs:
                try:
                    if job.type == "SCAN":
                        scan_executor.run(job)
                    elif job.type == "BACKUP":
                        backup_executor.run(job)
                    elif job.type == "RESTORE":
                        restore_executor.run(job)
                    else:
                        logging.warning("Unknown job type: %s", job.type)
                except Exception:
                    logging.exception("Failed to execute job %s", getattr(job, 'id', None))
        except Exception:
            logging.exception("Error pulling jobs from control plane")
        time.sleep(poll_interval)
