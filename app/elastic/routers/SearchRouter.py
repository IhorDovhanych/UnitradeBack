from fastapi import APIRouter, Query, Request
from fastapi.responses import RedirectResponse
from elastic.controllers import SearchController
from elastic.core import mapping_values
import starlette.status as status
from pydantic_models import ElasticIndexModel

router = APIRouter()

@router.post("/users")
async def search_users(req: Request, query: str = Query(..., min_length=1)):
    return await SearchController.search_users(request=req, query=query)

@router.post("/posts")
async def search_posts(req: Request, query: str = Query(..., min_length=1)):
    return await SearchController.search_posts(request=req, query=query)
