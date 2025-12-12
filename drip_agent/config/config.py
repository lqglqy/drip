import os


class AgentConfig:
    def __init__(self):
        self.control_plane_url = os.environ.get("CONTROL_PLANE_URL", "http://localhost:8080")
        self.poll_interval = int(os.environ.get("AGENT_POLL_INTERVAL", "5"))


def load_config() -> AgentConfig:
    return AgentConfig()
