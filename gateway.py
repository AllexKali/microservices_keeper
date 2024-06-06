from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

# Конфигурация URL микросервисов
AUTHENTICATION_SERVICE_URL = 'http://localhost:5001'
ORDERS_SERVICE_URL = 'http://localhost:5002'
MENU_SERVICE_URL = 'http://localhost:5003'
PAYMENT_SERVICE_URL = 'http://localhost:5004'

# Маршрутизация запросов к сервису аутентификации
@app.get("/register")
async def get_register(request: Request):
    response = requests.post(f'{AUTHENTICATION_SERVICE_URL}/register')
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return JSONResponse(content=response.json())
@app.post("/register")
async def post_register(request: Request):
    payload = await request.json()
    response = requests.post(f'{AUTHENTICATION_SERVICE_URL}/register', json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return JSONResponse(content=response.json())
@app.post("/login")
async def post_login(request: Request):
    payload = await request.json()
    response = requests.post(f'{AUTHENTICATION_SERVICE_URL}/login', json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return JSONResponse(content=response.json())
@app.get("/login")
async def get_login(request: Request):
    response = requests.get(f'{AUTHENTICATION_SERVICE_URL}/login')
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return JSONResponse(content=response.json())

@app.post("/admin")
async def post_admin(request: Request):
    payload = await request.json()
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

@app.post("/orders")
async def create_order(request: Request):
    payload = await request.json()
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
async def update_order(order_id: int, request: Request):
    payload = await request.json()
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

@app.post("/menu")
async def create_menu_item(request: Request):
    payload = await request.json()
    response = requests.post(f'{MENU_SERVICE_URL}/menu', json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return JSONResponse(content=response.json())

@app.get("/menu/{item_id}")
async def get_menu_item(item_id: int):
    response = requests.get(f'{MENU_SERVICE_URL}/menu/{item_id}')
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return JSONResponse(content=response.json())

@app.put("/menu/{item_id}")
async def update_menu_item(item_id: int, request: Request):
    payload = await request.json()
    response = requests.put(f'{MENU_SERVICE_URL}/menu/{item_id}', json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return JSONResponse(content=response.json())

@app.delete("/menu/{item_id}")
async def delete_menu_item(item_id: int):
    response = requests.delete(f'{MENU_SERVICE_URL}/menu/{item_id}')
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return JSONResponse(content=response.json())

# Маршрутизация запросов к сервису платежей
@app.post("/transactions")
async def create_transaction(request: Request):
    payload = await request.json()
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
    uvicorn.run(app, port=5000)
