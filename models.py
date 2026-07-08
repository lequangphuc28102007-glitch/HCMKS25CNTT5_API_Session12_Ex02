from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from database import Base

class DocumentModel(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    title: Mapped[str] = mapped_column(String(255), nullable=False)

    subject: Mapped[str] = mapped_column(String(100), nullable=False)

    document_type: Mapped[str] = mapped_column(String(100), nullable=False)

    file_url: Mapped[str] = mapped_column(String(500), nullable=False)