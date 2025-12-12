import logging
from drip_agent.client.models import Job
from drip_agent.scanner import content_scanner, metadata_scanner


def run(job: Job):
    logging.info("scan_executor running job=%s", job.id)
    # Minimal flow: scan metadata then content, compute simple result
    meta = metadata_scanner.scan(job.payload)
    content = content_scanner.scan(job.payload)
    result = {"meta": meta, "content_matches": content}
    logging.debug("scan result: %s", result)
    return result
