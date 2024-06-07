from fastapi import FastAPI, Request, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import requests
from pydantic import BaseModel

app = FastAPI()

# Конфигурация URL микросервисов
AUTHENTICATION_SERVICE_URL = 'http://authentication:5001'
ORDERS_SERVICE_URL = 'http://orders:5002'
MENU_SERVICE_URL = 'http://menu:5003'
PAYMENT_SERVICE_URL = 'http://transactions:5004'
# AUTHENTICATION_SERVICE_URL = 'http://authentication:5001'
# ORDERS_SERVICE_URL = 'http://orders:5002'
# MENU_SERVICE_URL = 'http://localhost:5003'
# PAYMENT_SERVICE_URL = 'http://transactions:5004'
@app.get("/")
async def root():
    return {"message": "Hello World"}


# Маршрутизация запросов к сервису аутентификации
@app.get("/register")
async def get_register():
    response = requests.get(f'{AUTHENTICATION_SERVICE_URL}/register')
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return JSONResponse(content=response.json())

class LodData(BaseModel):
    username: str
    password: str
@app.post("/register")
async def post_register(lodData: LodData):
    payload = jsonable_encoder(lodData)
    response = requests.post(f'{AUTHENTICATION_SERVICE_URL}/register', json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return JSONResponse(content=response.json())

@app.post("/login")
async def post_login(lodData: LodData):
    payload = jsonable_encoder(lodData)
    response = requests.post(f'{AUTHENTICATION_SERVICE_URL}/login', json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return JSONResponse(content=response.json())
@app.get("/login")
async def get_login():
    response = requests.get(f'{AUTHENTICATION_SERVICE_URL}/login')
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return JSONResponse(content=response.json())

class Admin(BaseModel):
    username: str
    role: int
@app.post("/admin")
async def post_admin(admin: Admin):
    payload = jsonable_encoder(admin)
    response = requests.post(f'{AUTHENTICATION_SERVICE_URL}/admin', json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return JSONResponse(content=response.json())
@app.get("/admin")
async def get_admin(request: Request):
    response = requests.get(f'{AUTHENTICATION_SERVICE_URL}/admin')
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return JSONResponse(content=response.json())

@app.get("/waiter")
async def get_none(request: Request):
    response = requests.get(f'{AUTHENTICATION_SERVICE_URL}/waiter/')
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return JSONResponse(content=response.json())

@app.get("/none")
async def get_none(request: Request):
    response = requests.get(f'{AUTHENTICATION_SERVICE_URL}/none/')
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return JSONResponse(content=response.json())

# Маршрутизация запросов к сервису заказов
@app.get("/orders")
async def get_orders():
    response = requests.get(f'{ORDERS_SERVICE_URL}/orders')
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return JSONResponse(content=response.json())

class Order(BaseModel):
    table_number: int
    items: str
    status: str

@app.post("/orders")
async def create_order(order: Order):
    payload = jsonable_encoder(order)
    response = requests.post(f'{ORDERS_SERVICE_URL}/orders', json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return JSONResponse(content=response.json())

@app.get("/orders/{order_id}")
async def get_order(order_id: int):
    response = requests.get(f'{ORDERS_SERVICE_URL}/orders/{order_id}')
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return JSONResponse(content=response.json())

@app.put("/orders/{order_id}")
async def update_order(order_id: int, order: Order):
    payload = jsonable_encoder(order)
    response = requests.put(f'{ORDERS_SERVICE_URL}/orders/{order_id}', json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return JSONResponse(content=response.json())

@app.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    response = requests.delete(f'{ORDERS_SERVICE_URL}/orders/{order_id}')
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return JSONResponse(content=response.json())

# Маршрутизация запросов к сервису меню
@app.get("/menu")
async def get_menu():
    response = requests.get(f'{MENU_SERVICE_URL}/menu')
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return JSONResponse(content=response.json())

class MenuItem(BaseModel):
    Category_id: int
    Name: str
    Weight: float
    Cost: int
    Amount: int
@app.post("/menu")
async def create_menu_item(menuItem: MenuItem):
    payload = jsonable_encoder(menuItem)
    response = requests.post(f'{MENU_SERVICE_URL}/menu', json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return JSONResponse(content=response.json())

@app.put("/menu/{item_id}")
async def update_menu_item(item_id: int, menuItem: MenuItem):
    payload = jsonable_encoder(menuItem)
    response = requests.put(f'{MENU_SERVICE_URL}/menu/{item_id}', json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return JSONResponse(content=response.json())

@app.delete("/menu/{item_id}")
async def delete_menu_item(item_id: str):
    response = requests.delete(f'{MENU_SERVICE_URL}/menu/{item_id}')
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return JSONResponse(content=response.json())

# Маршрутизация запросов к сервису платежей

class Transactions(BaseModel):
    amount: float
@app.post("/transactions")
async def create_transaction(transactions: Transactions):
    payload = jsonable_encoder(transactions)
    # print(payload)
    response = requests.post(f'{PAYMENT_SERVICE_URL}/transactions', json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return JSONResponse(content=response.json())

@app.get("/transactions")
async def get_transactions():
    response = requests.get(f'{PAYMENT_SERVICE_URL}/transactions')
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return JSONResponse(content=response.json())

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0",  port=5000)
    # uvicorn.run(app, port=5000)
