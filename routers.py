from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas import (
    DocumentCreate,
    DocumentResponse,
    MessageResponse
)
from services import (
    get_all_documents,
    create_document,
    delete_document
)

router = APIRouter()


@router.get(
    "/documents",
    response_model=list[DocumentResponse]
)
def get_documents(db: Session = Depends(get_db)):
    return get_all_documents(db)


@router.post(
    "/documents",
    response_model=DocumentResponse,
    status_code=201
)
def add_document(
    document: DocumentCreate,
    db: Session = Depends(get_db)
):
    return create_document(document, db)


@router.delete(
    "/documents/{document_id}",
    response_model=MessageResponse
)
def remove_document(
    document_id: int,
    db: Session = Depends(get_db)
):
    return delete_document(document_id, db)