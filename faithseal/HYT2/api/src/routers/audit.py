from fastapi import APIRouter, Depends
from ..models.audit import AuditRequest, AuditResponse
from ..services.ethics_sentinel import EthicsSentinel, get_ethics_sentinel

router = APIRouter()

@router.post("/audit/text", response_model=AuditResponse)
async def audit_text(
    request: AuditRequest,
    sentinel: EthicsSentinel = Depends(get_ethics_sentinel)
):
    return sentinel.analyze_text(request.text)
