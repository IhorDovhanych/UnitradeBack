from fastapi import Query, Request, HTTPException

from elastic.controllers import DocumentsController


class SearchController:
    def __init__(self) -> None:
        pass

    @staticmethod
    async def search_posts(request: Request, query: str = Query(..., min_length=1)):
        search_results = await DocumentsController.search_document_by_text(
            request=request, index_name="posts", text=query
        )
        if not search_results:
            raise HTTPException(
                status_code=404, detail="No posts found matching the search query"
            )
        return search_results

    @staticmethod
    async def search_users(request: Request, query: str = Query(..., min_length=1)):
        search_results = await DocumentsController.search_document_by_text(
            request=request, index_name="users", text=query, fields=["name", "email"]
        )
        if not search_results:
            raise HTTPException(
                status_code=404, detail="No users found matching the search query"
            )
        return search_results
