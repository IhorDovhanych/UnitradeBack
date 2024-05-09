from fastapi import Request, HTTPException


class IndicesController:
    def __init__(self) -> None:
        pass

    @staticmethod
    async def create_index(request: Request, name, body) -> dict:
        elastic_client = request.app.state.elastic_client
        await elastic_client.indices.create(index=name, body=body, ignore=400)
        return {"success": True, "name": name, "body": body}

    @staticmethod
    async def create_several_indices(request: Request, mapping_values: dict) -> dict:
        elastic_client = request.app.state.elastic_client
        for key, value in mapping_values.items():
            await elastic_client.indices.create(index=key, body=value, ignore=400)
        return {"success": True}
    
    @staticmethod
    async def delete_index(request: Request, name) -> dict:
        elastic_client = request.app.state.elastic_client
        try:
            await elastic_client.indices.delete(index=name, ignore=400)
            return {"success": True, "name": name}
        except:
            return HTTPException(400, "index not found")
