from fastapi import APIRouter, HTTPException
from ecommerce.modules.cart import cart

router = APIRouter(prefix="/orders", tags=["Orders"])

orders = []
next_order_id = 1

@router.post("/")
def make_order():
    global next_order_id

    if not cart:
        raise HTTPException(status_code=400, detail="Cart is empty")
    
    total = sum(item["price"] for item in cart)

    order = {
        "id" : next_order_id,
        "items" : cart.copy(),
        "price" : total
    }

    orders.append(order)
    cart.clear()
    next_order_id += 1

    return order

@router.get("/")
def get_orders():
    return orders

@router.get("/{id}")
def get_order_id(order_id : int):
    for order in orders:
        if (order["id"] == order_id):
            return order
        
    raise HTTPException(status_code=404, detail="Order ID not found")
