from fastapi import APIRouter, Query, Request
from elastic.controllers import SearchController

router = APIRouter()

@router.post("/users")
async def search_users(req: Request, query: str = Query(..., min_length=1)):
    return await SearchController.search_users(request=req, query=query)

@router.post("/posts")
async def search_posts(req: Request, query: str = Query(..., min_length=1)):
    return await SearchController.search_posts(request=req, query=query)
