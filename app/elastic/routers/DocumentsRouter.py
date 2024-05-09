from fastapi import APIRouter, Request
from elastic.controllers import DocumentsController
from pydantic_models import ElasticDocumentModel

router = APIRouter()

@router.post('/create')
async def create_document(req: Request, name: str, document: ElasticDocumentModel):
    print(document.body)
    await DocumentsController.create_document(req, name, document.body)