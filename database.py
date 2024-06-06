#для orders
import requests

data = {
    'table_number': 3,
    'items': 'Item 5, Item 6',
}

response = requests.post('http://localhost:5000/orders', json=data)
print(response.status_code)  # output 201
