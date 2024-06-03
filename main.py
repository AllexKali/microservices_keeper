from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)
food = ['Drinks', 'Main dishes', 'Soups', 'Salads', 'Desserts']


def display_menu(menu):
    res_menu = {}
    prev_id = 1
    category_food = {}
    counter = 1
    for j in range(len(menu)):
        if prev_id != menu[j][0]:
            counter = 1
            res_menu[food[prev_id-1]] = category_food
            category_food = {}
            prev_id = menu[j][0]
        if menu[j][6] != 0:
            curr_food = {}
            curr_food["Name"] = menu[j][3]
            curr_food["Weight/Volume"] = menu[j][4]
            curr_food["Cost"] = menu[j][5]
            category_food[counter] = curr_food
            counter += 1
    res_menu[food[prev_id - 1]] = category_food
    # print(res_menu)
    return res_menu


# Получение всего меню
@app.route('/menu', methods=['GET'])
def get_menu():
    connection = sqlite3.connect("databases/menu.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Categories JOIN Soups on Category_id == Categories.Id \
        UNION\
         SELECT * FROM Categories JOIN Salads on Category_id == Categories.Id\
         UNION\
         SELECT * FROM Categories JOIN [Main dishes] on Category_id == Categories.Id\
         UNION\
         SELECT * FROM Categories JOIN Desserts on Category_id == Categories.Id\
         UNION\
         SELECT * FROM Categories JOIN Drinks on Category_id == Categories.Id')
    menu = cursor.fetchall()
    res_menu = display_menu(menu)
    print(res_menu)
    connection.close()
    return jsonify(res_menu)


# Добавление блюда в меню
@app.route('/menu', methods=['POST'])
def add_dish():
    data = request.get_json()
    connection = sqlite3.connect("databases/menu.db")
    cursor = connection.cursor()
    curr_request = 'SELECT max(Id) FROM ' + str(food[data["Category_id"]-1])
    cursor.execute(curr_request)
    id = cursor.fetchall()[0][0]
    connection.close()
    connection = sqlite3.connect("databases/menu.db")
    cursor = connection.cursor()
    curr_request = 'INSERT INTO ' + str(food[data["Category_id"]-1]) + ' VALUES(' + str(id+1) + ", '" + data['Name'] +\
        "', " + str(data['Weight/Volume']) + ', ' + str(data['Cost']) + ', 1, ' + str(data['Category_id']) + ')'
    print("ADD", curr_request)
    cursor.execute(curr_request)
    connection.commit()
    connection.close()
    return jsonify({"message": "Dish added successfully"})


# Удаление блюда из меню
@app.route('/menu/<dish_id_category>', methods=['DELETE'])
def delete_dish(dish_id_category):
    connection = sqlite3.connect("databases/menu.db")
    cursor = connection.cursor()
    dish_id_category = dish_id_category.split(",")
    dish_id, category_id = int(dish_id_category[0][1:]), int(dish_id_category[1][1:-1])
    curr_request = 'DELETE FROM ' + str(food[category_id - 1]) + ' WHERE Id = ' + str(dish_id)
    print("DEL", curr_request)
    cursor.execute(curr_request)
    connection.commit()
    connection.close()
    return jsonify({"message": "Dish deleted successfully"})


# Обновление блюда в меню
@app.route('/menu/<dish_id>', methods=['PUT'])
def update_dish(dish_id):
    data = request.get_json()
    connection = sqlite3.connect("databases/menu.db")
    cursor = connection.cursor()
    category_id = data['Category_id']
    if food[category_id - 1] == 'Drinks':
        curr_request = 'UPDATE ' + str(food[category_id - 1]) + ' SET Name = ' + "'" + data['Name'] +\
            "', Volume = " + str(data['Weight/Volume']) + ', Cost = ' + str(data['Cost']) + ', Amount = ' + str(data['Amount']) +\
            ' WHERE Id = ' + str(dish_id)
    else:
        curr_request = 'UPDATE ' + str(food[category_id - 1]) + ' SET Name = ' + "'" + data['Name'] + \
            "', Weight = " + str(data['Weight/Volume']) + ', Cost = ' + str(data['Cost']) + ', Amount = ' + str(data['Amount']) + \
            ' WHERE Id = ' + str(dish_id)
    print("UPDATE", curr_request)
    cursor.execute(curr_request)
    connection.commit()
    connection.close()
    return jsonify({"message": "Dish updated successfully"})


if __name__ == '__main__':
    app.run(debug=True)
