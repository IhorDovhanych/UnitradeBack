from fastapi import Request, HTTPException


class DocumentsController:
    def __init__(self) -> None:
        pass

    @staticmethod
    async def create_document(request: Request, name, body) -> dict:
        elastic_client = request.app.state.elastic_client
        await elastic_client.index(index=name, document=body, ignore=400)
        return {"success": True, "name": name, "body": body}