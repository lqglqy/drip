import os
import uuid
import logging
from drip_agent.utils.logging import setup_logging
from drip_agent.client.control_plane_client import ControlPlaneClient
from drip_agent.scheduler.worker_loop import run as run_worker


def main():
    setup_logging()
    agent_id = os.environ.get("AGENT_ID") or str(uuid.uuid4())
    control_plane_url = os.environ.get("CONTROL_PLANE_URL", "http://localhost:8080")
    logging.info("Starting drip_agent with id=%s", agent_id)

    client = ControlPlaneClient(control_plane_url)
    try:
        run_worker(agent_id, client)
    except KeyboardInterrupt:
        logging.info("drip_agent shutting down")


if __name__ == "__main__":
    main()
