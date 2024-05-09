from fastapi import Response, HTTPException, status
from sqlalchemy import or_
from sqlalchemy.orm import joinedload

import shutil
import os
from dotenv import load_dotenv

from models import Post, Image, Category


load_dotenv("../.env")
images_dir = os.environ.get("IMAGES_DIR")


class PostController:
    @staticmethod
    async def get_posts(page, limit, filter_, sort_, db):
        def get_filter_statement(column, query: list[str]):
            filter_statement = or_(*[column == value for value in query])
            return filter_statement

        def get_sort_statement(model, query: str):
            column, order = query.split()
            sort_statement = getattr(getattr(model, column), order)()
            return sort_statement

        filter_statement = get_filter_statement(Category.name, filter_)
        sort_statement = get_sort_statement(Post, sort_)

        posts = (
            db.query(Post)
            .join(Post.images)
            .join(Post.categories)
            .filter(
                Post.display,
                filter_statement,
            )
            .order_by(
                sort_statement,
            )
            .limit(limit)
            .offset(page * limit)
            .options(
                joinedload(Post.images),
                joinedload(Post.categories),
            )
            .all()
        )

        return {"response": posts}

    @staticmethod
    async def get_post(id, db):
        post = (
            db.query(Post)
            .join(Post.images)
            .filter(Post.id == id)
            .options(
                joinedload(Post.images),
                joinedload(Post.categories),
            )
            .first()
        )

        if post is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post with such id not found")
        else:
            return {"response": post}

    @staticmethod
    async def create_post(item, categories, db):
        post = Post(**item.dict())
        db.add(post)
        db.commit()

        # for f in files:
        #     image = Image(post_id=post.id)
        #     db.add(image)

        #     image = db.query(Image).order_by(Image.id.desc()).first()
        #     path = f"{post.id}_{image.id}.jpg"
        #     image.url = path

        #     with open(images_dir + path, "wb") as buffer:
        #         shutil.copyfileobj(f.file, buffer)
        # else:
        #     db.commit()

        for c in categories:
            category = Category(post_id=post.id, name=c)
            db.add(category)
        else:
            db.commit()

        return post

    @staticmethod
    async def update_post(id, item, db):
        post = db.query(Post).filter(Post.id == id)
        if post.first() is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post with such id not found")
        else:
            post.update(item.dict())
            db.commit()

        return Response("Successfully updated", 200)

    @staticmethod
    async def delete_post(id, db):
        post = db.query(Post).get(id)
        if post is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post with such id not found")
        else:
            db.delete(post)
            db.commit()

        return Response("Successfully deleted", 200)

    @staticmethod
    async def add_image(id, files, db):
        for file in files:
            image = Image(post_id=id)
            db.add(image)

            image = db.query(Image).order_by(Image.id.desc()).first()
            path = f"{id}_{image.id}.jpg"
            image.url = path

            with open(images_dir + path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
        else:
            db.commit()

        return Response("Successfully created", 201)

    @staticmethod
    async def delete_image(id, db):
        image = db.query(Image).get(id)
        if image is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Image with such id not found")
        else:
            db.delete(image)
            db.commit()

        return Response("Successfully deleted", 200)

    @staticmethod
    async def add_category(id, categories, db):
        for c in categories:
            category = Category(post_id=id, name=c)
            db.add(category)
        else:
            db.commit()

        return Response("Successfully created", 201)

    @staticmethod
    async def delete_category(id, db):
        category = db.query(Category).get(id)
        if category is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="category with such id not found")
        else:
            db.delete(category)
            db.commit()

        return Response("Successfully deleted", 200)
