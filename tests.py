import requests

# response = requests.get('http://127.0.0.1:5000/menu')
# print(response.status_code)

menu = {"1": {"name": "Pizza", "price": 10}, "2": {"name": "Pasta", "price": 8}, "3": {"name": "Salad", "price": 6}}

def test_get_menu():
    response = requests.get('http://127.0.0.1:5000/menu')
    assert response.status_code == 200
    assert response.json() == menu


def test_add_dish():
    new_dish = {"name": "Burger", "price": 12}
    response = requests.post('http://127.0.0.1:5000/menu', json=new_dish)
    assert response.status_code == 200
    assert response.json() == {"message": "Dish added successfully"}


def test_update_dish():
    updated_dish = {"name": "Pizza", "price": 15}
    dish_id = "1"  # предположим, что обновляем первое блюдо
    response = requests.put(
        f'http://127.0.0.1:5000/menu/{dish_id}',
        json=updated_dish
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Dish updated successfully"}


def test_delete_dish():
    dish_id = "3"  # предположим, что удаляем третье блюдо
    response = requests.delete(f'http://127.0.0.1:5000/menu/{dish_id}')
    assert response.status_code == 200
    # Дополнительная проверка может быть на отсутствие удаленного блюда в меню
    assert dish_id not in response.json().keys()


test_get_menu()
test_add_dish()
#test_update_dish()
#test_delete_dish()
