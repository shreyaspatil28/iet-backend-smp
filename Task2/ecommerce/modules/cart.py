from fastapi import APIRouter, HTTPException
from ecommerce.modules.products import products

router = APIRouter(prefix="/cart", tags=["Cart"])

cart = []

@router.get("/")
def get_cart():
    return cart

@router.post("/add/{product_id}")
def add_to_cart(product_id : int):
    product = next((p for p in products if p["id"] == product_id), None)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    cart.append(product)

    return {"message" : "Added to cart", "product":product}

@router.delete("/remove/{product_id}")
def remove_from_cart(product_id : int):
    for item in cart:
        if (item["id"] == product_id):
            cart.remove(item)
            return {"message":"Removed from cart"}
        
    raise HTTPException(status_code=404, detail="Product not found in cart")


