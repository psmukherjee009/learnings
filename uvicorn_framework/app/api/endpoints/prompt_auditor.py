from fastapi import APIRouter
import logging
from app.api.core.formatting import LogFormatter

from app.api.service.prompt_auditor_service import PromptAuditorService

logger = logging.getLogger(__name__)
router = APIRouter()
prompt_auditor_service = PromptAuditorService()

@router.get("/hello")
async def get_hello():
    """
    Get formatted prompt data with restructured objects
    Response will be automatically GZIP compressed if size > 500 bytes
    """
    try:
        return {"Hello": prompt_auditor_service.get_hello_string()}
    except Exception as e:
        logger.error(LogFormatter.error("Error restarting Prompt Validator file watch", e))

@router.get("/ping")
async def ping():
    # An asynchronous operation could happen here, e.g., checking database connection
    # result = await database.check_health()
    return {"ping": "pong!"}
