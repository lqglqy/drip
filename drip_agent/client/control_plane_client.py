import logging
from typing import List
from drip_agent.client.models import Job


class ControlPlaneClient:
    """Simple placeholder client for pulling jobs and reporting results.

    Replace with real HTTP/gRPC client to the control plane.
    """

    def __init__(self, base_url: str):
        self.base_url = base_url

    def pull_jobs(self, agent_id: str) -> List[Job]:
        # TODO: implement HTTP/gRPC call to control plane. Return list of Job
        logging.debug("pull_jobs called for agent=%s", agent_id)
        return []

    def report_result(self, job_id: str, result: dict) -> None:
        # TODO: implement report
        logging.debug("report_result job=%s result=%s", job_id, result)
