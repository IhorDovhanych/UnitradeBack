from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from elastic.controllers import IndicesController
from elastic.core import mapping_values
import starlette.status as status
from pydantic_models import ElasticIndexModel

router = APIRouter()


@router.get("/open")
def redirect_to_elastic_search():
    return RedirectResponse(
        url="http://localhost:9200", status_code=status.HTTP_302_FOUND
    )


@router.get("/open_kibana")
def redirect_to_elastic_search():
    return RedirectResponse(
        url="http://localhost:5601", status_code=status.HTTP_302_FOUND
    )


@router.post("/create/default")
async def create_default_indices(req: Request):
    await IndicesController.create_several_indices(
        req, mapping_values.INDICES_FOR_MAPPING
    )


@router.post("/create")
async def create_index(item: ElasticIndexModel, req: Request):
    await IndicesController.create_index(req, item.name, item.body)


@router.delete("/delete")
async def create_index(name: str, req: Request):
    await IndicesController.delete_index(req, name)
