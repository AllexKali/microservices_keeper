import sqlite3

connection = sqlite3.connect("databases/menu.db")
cursor = connection.cursor()
cursor.execute('SELECT * FROM Categories')
category = cursor.fetchall()
print(category)
connection.close()

# cursor.execute('SELECT * FROM Categories JOIN Soups on Category_id == Categories.Id \
#     UNION\
#     SELECT * FROM Categories JOIN Salads on Category_id == Categories.Id\
#     UNION\
#     SELECT * FROM Categories JOIN [Main dishes] on Category_id == Categories.Id\
#     UNION\
#     SELECT * FROM Categories JOIN Desserts on Category_id == Categories.Id\
#     UNION\
#     SELECT * FROM Categories JOIN Drinks on Category_id == Categories.Id')
#     menu = cursor.fetchall()
