from pydantic import BaseModel


class DocumentCreate(BaseModel):
    title: str
    subject: str
    document_type: str
    file_url: str


class DocumentResponse(BaseModel):
    id: int
    title: str
    subject: str
    document_type: str
    file_url: str

    model_config = {
        "from_attributes": True
    }


class MessageResponse(BaseModel):
    success: bool
    message: str