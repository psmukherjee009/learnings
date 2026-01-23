import logging

from app.api.core.formatting import LogFormatter

logger = logging.getLogger(__name__)

class PromptAuditorService:
    def __init__(self):
        pass

    def get_hello_string(self):
        return "Brad"