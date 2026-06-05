from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/categories", tags=["Categories"])

class Category(BaseModel):
    name : str

categories = []
next_cat_id = 1

@router.get("/")
def list_categories():
    return categories

@router.post("/")
def add_category(category : Category):
    global next_cat_id

    new_category = {"id" : next_cat_id, **category.model_dump()}

    categories.append(new_category)
    next_cat_id += 1

    return new_category

