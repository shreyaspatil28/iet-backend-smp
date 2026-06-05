from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/products", tags=["Product"])

products = []
next_prod_id = 1

class Product(BaseModel):
    name : str
    price : float
    category_id : int

@router.get("/")
def get_products():
    return products

@router.get("/{id}")
def get_product_id(product_id : int):
    for product in products:
        if (product["id"] == product_id):
            return product
        
    raise HTTPException(status_code=404, detail="Product not found")
        
@router.post("/")
def create_product(product : Product):
    global next_prod_id

    new_prod = {"id":next_prod_id, **product.model_dump()}

    products.append(new_prod)
    next_prod_id += 1

    return new_prod;

@router.put("/{id}")
def update_product(product_id : int, update_prod : Product):
    for product in products:
        if (product["id"] == product_id):
            product.update(update_prod.model_dump())
            return product
        
    raise HTTPException(status_code=404, detail="Product not found")
        
@router.delete("/{id}")
def delete_product(product_id : int):
    for product in products:
        if (product["id"] == product_id):
            products.remove(product)
            return {"message" : "Product deleted"}
        
    raise HTTPException(status_code=404, detail="Product not found")
        





