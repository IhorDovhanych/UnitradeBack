from fastapi import APIRouter, HTTPException, Request
from elastic.controllers import DocumentsController
from pydantic_models import ElasticDocumentModel

router = APIRouter()

@router.post('/create')
async def create_document(req: Request, name: str, document: ElasticDocumentModel):
    return await DocumentsController.create_document(req, name, document.body)

@router.delete('/delete')
async def delete_document(req: Request, name: str, document_id: str):
    return await DocumentsController.delete_document(req, name, document_id)

@router.put('/update')
async def create_document(req: Request, name: str, document_id: str, document: ElasticDocumentModel):
    return await DocumentsController.update_document(req, name, document_id, document.body)