from fastapi import APIRouter

from app.api.endpoints import prompt_auditor

router = APIRouter()

router.include_router(prompt_auditor.router, prefix="/api", tags=["prompt_auditor"])