from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

menu = {"1": {"name": "Pizza", "price": 10}, "2": {"name": "Pasta", "price": 8}, "3": {"name": "Salad", "price": 6}}


# Получение всего меню
@app.route('/menu', methods=['GET'])
def get_menu():
    return jsonify(menu)


# Добавление блюда в меню
@app.route('/menu', methods=['POST'])
def add_dish():
    data = request.get_json()
    dish_id = str(len(menu) + 1)
    menu[dish_id] = {"name": data['name'], "price": data['price']}
    return jsonify({"message": "Dish added successfully"})


# Обновление блюда в меню
@app.route('/menu/<dish_id>', methods=['PUT'])
def update_dish(dish_id):
    data = request.get_json()
    menu[dish_id] = {"name": data['name'], "price": data['price']}
    return jsonify({"message": "Dish updated successfully"})


# Удаление блюда из меню
@app.route('/menu/<dish_id>', methods=['DELETE'])
def delete_dish(dish_id):
    del menu[dish_id]
    return jsonify({"message": "Dish deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True)

