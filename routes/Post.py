from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Response
from sqlalchemy.orm import Session
from sqlalchemy import func
from models import Post, PostModel, Image
from session import get_session
import shutil
from typing import Annotated

router = APIRouter(prefix="/api/posts", tags=["Posts CRUD API"])
images_dir = "images/"


@router.get("/")
async def get_posts(db: Session = Depends(get_session)):
    posts = db.query(Post).all()
    images = db.query(func.min(Image.id), Image).group_by(Image.post_id)
    images = [obj[1] for obj in images]

    return {
        "post": posts,
        "images": images,
    }


@router.get("/{id}")
async def get_post(id: int, db: Session = Depends(get_session)):
    post = db.query(Post).get(id)
    images = db.query(Image).where(Image.post_id == id).all()

    return {
        "post": post,
        "images": images,
    }


@router.post("/create")
async def create_post(
        files: Annotated[list[UploadFile], File(...)],
        item: PostModel = Depends(),
        db: Session = Depends(get_session),
):
    post = Post(**item.dict())
    db.add(post)
    db.commit()

    for file in files:
        image = Image(post_id=post.id)
        db.add(image)

        image = db.query(Image).order_by(Image.id.desc()).first()
        path = f"{post.id}_{image.id}.jpg"
        image.url = path

        with open(images_dir + path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    else:
        db.commit()

    return Response("Successfully created", 201)


@router.put("/update/{id}")
async def update_post(id: int, item: PostModel, db: Session = Depends(get_session)):
    post = db.query(Post).get(id)
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post with such id not found")
    else:
        post.title = item.title
        post.description = item.description
        db.commit()

    return Response("Successfully updated", 200)


@router.delete("/delete/{id}")
async def delete_post(id: int, db: Session = Depends(get_session)):
    post = db.query(Post).get(id)
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post with such id not found")
    else:
        db.delete(post)
        db.commit()

    return Response("Successfully deleted", 200)


@router.post("/image/add/{id}")
async def add_image(
        files: Annotated[list[UploadFile], File(...)],
        post_id: int,  # post id
        db: Session = Depends(get_session),
):
    for file in files:
        image = Image(post_id=post_id)
        db.add(image)

        image = db.query(Image).order_by(Image.id.desc()).first()
        path = f"{post_id}_{image.id}.jpg"
        image.url = path

        with open(images_dir + path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    else:
        db.commit()

    return Response("Successfully created", 201)


@router.delete("/image/delete/{id}")
async def delete_image(id: int, db: Session = Depends(get_session)):
    image = db.query(Image).get(id)
    if image is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Image with such id not found")
    else:
        db.delete(image)
        db.commit()

    return Response("Successfully deleted", 200)
