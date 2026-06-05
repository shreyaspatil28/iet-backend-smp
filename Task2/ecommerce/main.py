from fastapi import FastAPI
from ecommerce.modules.products import router as products_router
from ecommerce.modules.categories import router as categories_router
from ecommerce.modules.cart import router as cart_router
from ecommerce.modules.orders import router as orders_router

app = FastAPI()

app.include_router(products_router)
app.include_router(categories_router)
app.include_router(cart_router)
app.include_router(orders_router)
