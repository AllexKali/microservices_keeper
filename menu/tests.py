import requests

# response = requests.get('http://127.0.0.1:5000/menu')
# print(response.status_code)


def test_get_menu():
    response = requests.get('http://127.0.0.1:5000/menu')
    assert response.status_code == 200
    # assert response.json() == menu


def test_add_dish():
    new_dish = {'Name': 'Cocacol', 'Weight_or_Volume': 200.0, 'Cost': 350, 'Category_id': 1}
    response = requests.post('http://127.0.0.1:5000/menu', json=new_dish)
    assert response.status_code == 200
    assert response.json() == {"message": "Dish added successfully"}


def test_update_dish():
    updated_dish = {"Name": "Coffee", 'Weight/Volume': 200.0, 'Cost': 350, 'Amount': 3, 'Category_id': 1}
    dish_id = 22
    response = requests.put(
        f'http://127.0.0.1:5000/menu/{dish_id}',
        json=updated_dish
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Dish updated successfully"}


def test_delete_dish():
    dish_id_category = [22, 1]
    response = requests.delete(f'http://127.0.0.1:5000/menu/{dish_id_category}')
    assert response.status_code == 200
    # Дополнительная проверка может быть на отсутствие удаленного блюда в меню
    assert response.json() == {"message": "Dish deleted successfully"}

test_get_menu()
# test_add_dish()
# test_update_dish()
# test_delete_dish()
