from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from schemas.url_schema import URLCreate, URLResponse
from service.url_service import URLService
from db.database import get_db

router = APIRouter()
service = URLService()

@router.post("/shorten", response_model=URLResponse)
def create_short_url(request_body: URLCreate, request: Request, db: Session = Depends(get_db)):
    short_url = service.create_short_url(db, request_body, request)
    return {"short_url": short_url}

@router.get("/{code}")
def redirect_url(code: str, db: Session = Depends(get_db)):
    full_url = service.resolve_url(db, code)
    return RedirectResponse(full_url, status_code=302)