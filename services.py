from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models import DocumentModel
from schemas import DocumentCreate


def get_all_documents(db: Session):
    return db.query(DocumentModel).all()


def create_document(data: DocumentCreate, db: Session):
    document = DocumentModel(
        title=data.title,
        subject=data.subject,
        document_type=data.document_type,
        file_url=data.file_url
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return document


def delete_document(document_id: int, db: Session):

    document = db.query(DocumentModel).filter(
        DocumentModel.id == document_id
    ).first()

    if document is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found."
        )

    db.delete(document)
    db.commit()

    return {
        "success": True,
        "message": "Delete successfully."
    }