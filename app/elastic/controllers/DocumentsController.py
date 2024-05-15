from typing import List
from fastapi import Request, HTTPException


class DocumentsController:
    def __init__(self) -> None:
        pass

    @staticmethod
    async def create_document(request: Request, name: str, body: str) -> dict:
        elastic_client = request.app.state.elastic_client
        await elastic_client.index(index=name, document=body)
        return {"success": True, "name": name, "body": body}

    @staticmethod
    async def delete_document(request: Request, name: str, document_id: str) -> dict:
        elastic_client = request.app.state.elastic_client
        try:
            response = await elastic_client.delete(index=name, id=document_id)
            if response["result"] == "deleted":
                return {
                    "success": True,
                    "message": f"Document with ID {document_id} deleted successfully",
                }
            else:
                return {"success": False, "message": "Failed to delete document"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    async def update_document(
        request: Request, name: str, document_id: str, body: str
    ) -> dict:
        elastic_client = request.app.state.elastic_client
        try:
            response = await elastic_client.update(
                index=name, id=document_id, body={"doc": body}
            )
            if response["result"] == "updated":
                return {
                    "success": True,
                    "message": f"Document with ID {document_id} updated successfully",
                }
            else:
                return {"success": False, "message": "Failed to update document"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    async def search_document_by_field(
        request: Request, name: str, field: str, value: str
    ) -> dict:
        try:
            elastic_client = request.app.state.elastic_client
            response = await elastic_client.search(
                index=name, body={"query": {"match": {field: value}}}
            )
            hits = response["hits"]["hits"]
            if hits:
                return hits[0]["_source"]
            else:
                return None
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    async def search_document_by_field_with_id(
        request: Request, name: str, field: str, value: str
    ) -> dict:
        try:
            elastic_client = request.app.state.elastic_client
            response = await elastic_client.search(
                index=name, body={"query": {"match": {field: value}}}
            )
            hits = response["hits"]["hits"]
            if hits:
                return hits[0]["_id"]
            else:
                return None
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    async def search_document_by_text(
        request: Request, index_name: str, text: str, fields: List[str] = None
    ) -> List[dict]:
        elastic_client = request.app.state.elastic_client
        try:
            if fields is None:
                fields = ["title", "description"]
            body = {
            "query": {"multi_match": {"query": text, "fields": fields}},
            
        }
            response = await elastic_client.search(index=index_name, body=body)
            hits = response["hits"]["hits"]
            return [hit["_source"] for hit in hits]
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
