from decimal import Decimal
from fastapi import APIRouter, Depends, Request, Response, UploadFile, Query
from sqlalchemy.orm import Session

from models import PostModel
from controllers import PostController
from core.session import get_session

from elastic.controllers import DocumentsController

router = APIRouter()


@router.get("/")
async def get_posts(
    page: int = 0,
    limit: int = 10,
    filter_: list[str] = Query([], alias="filter"),
    sort_: str = Query("created_at desc", alias="sort"),
    db: Session = Depends(get_session),
):
    return await PostController.get_posts(page, limit, filter_, sort_, db)


@router.get("/{id}")
async def get_post(id: int, db: Session = Depends(get_session)):
    return await PostController.get_post(id, db)


@router.post("/create")
async def create_post(
    req: Request,
    item: PostModel,
    categories: list[str] = Query([]),
    db: Session = Depends(get_session),
):
    post = await PostController.create_post(item, categories, db)
    await DocumentsController.create_document(
        req,
        "posts",
        {
            "post_id": post.id,
            "title": item.title,
            "description": item.description,
            "display": item.display,
            "price": float(item.price),
            "user_id": str(item.user_id),
        },
    )
    return Response("Successfully created", 201)


@router.put("/update/{id}")
async def update_post(
    req: Request, id: int, item: PostModel, db: Session = Depends(get_session)
):
    document_id = await DocumentsController.search_document_by_field_with_id(
        req, "posts", "post_id", id
    )
    await DocumentsController.update_document(
        name="posts",
        document_id=document_id,
        body={
            "title": item.title,
            "description": item.description,
            "display": item.display,
            "price": float(item.price),
            "user_id": str(item.user_id),
        },
    )
    return await PostController.update_post(id, item, db)


@router.delete("/delete/{id}")
async def delete_post(req: Request, id: int, db: Session = Depends(get_session)):
    document_id = await DocumentsController.search_document_by_field_with_id(
        req, "posts", "post_id", id
    )
    await DocumentsController.delete_document(req, name="posts", document_id=document_id)

    return await PostController.delete_post(id, db)


@router.post("/image/add/{id}")
async def add_image(
    id: int, files: list[UploadFile], db: Session = Depends(get_session)
):
    return await PostController.add_image(id, files, db)


@router.delete("/image/delete/{id}")
async def delete_image(id: int, db: Session = Depends(get_session)):
    return await PostController.delete_image(id, db)


@router.post("/category/add/{id}")
async def add_category(
    id: int, categories: list[str] = Query([]), db: Session = Depends(get_session)
):
    return await PostController.add_category(id, categories, db)


@router.delete("/category/delete/{id}")
async def delete_category(id: int, db: Session = Depends(get_session)):
    return await PostController.delete_category(id, db)
