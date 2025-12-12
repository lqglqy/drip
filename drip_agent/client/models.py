from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class Job:
    id: str
    type: str
    payload: Dict[str, Any]


@dataclass
class JobResult:
    job_id: str
    status: str
    details: Dict[str, Any]
