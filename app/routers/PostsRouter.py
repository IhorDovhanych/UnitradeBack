from fastapi import APIRouter, Depends, UploadFile, Query
from sqlalchemy.orm import Session

from models import PostModel
from controllers import PostController
from core.session import get_session

PostsRouter = APIRouter(prefix="/api/posts", tags=["Posts API"])


@PostsRouter.get("/")
async def get_posts(
        page: int = 0,
        limit: int = 10,
        filter_: list[str] = Query([], alias="filter"),
        sort_: str = Query("created_at desc", alias="sort"),
        db: Session = Depends(get_session),
):
    return await PostController.get_posts(page, limit, filter_, sort_, db)


@PostsRouter.get("/{id}")
async def get_post(id: int, db: Session = Depends(get_session)):
    return await PostController.get_post(id, db)


@PostsRouter.post("/create")
async def create_post(
        item: PostModel = Depends(),
        files: list[UploadFile] = None,
        categories: list[str] = Query([]),
        db: Session = Depends(get_session),
):
    return await PostController.create_post(item, files, categories, db)


@PostsRouter.put("/update/{id}")
async def update_post(id: int, item: PostModel, db: Session = Depends(get_session)):
    return await PostController.update_post(id, item, db)


@PostsRouter.delete("/delete/{id}")
async def delete_post(id: int, db: Session = Depends(get_session)):
    return await PostController.delete_post(id, db)


@PostsRouter.post("/image/add/{id}")
async def add_image(id: int, files: list[UploadFile], db: Session = Depends(get_session)):
    return await PostController.add_image(id, files, db)


@PostsRouter.delete("/image/delete/{id}")
async def delete_image(id: int, db: Session = Depends(get_session)):
    return await PostController.delete_image(id, db)


@PostsRouter.post("/category/add/{id}")
async def add_category(id: int, categories: list[str] = Query([]), db: Session = Depends(get_session)):
    return await PostController.add_category(id, categories, db)


@PostsRouter.delete("/category/delete/{id}")
async def delete_category(id: int, db: Session = Depends(get_session)):
    return await PostController.delete_category(id, db)
