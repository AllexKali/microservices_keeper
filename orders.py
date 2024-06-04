from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
db = SQLAlchemy(app)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_number = db.Column(db.Integer)
    items = db.Column(db.String)
    status = db.Column(db.String)

    def to_json(self):
        return {
            'id': self.id,
            'table_number': self.table_number,
            'items': self.items,
            'status': self.status
        }

@app.route('/orders', methods=['GET', 'POST'])
def orders():
    if request.method == 'GET':
        orders = Order.query.all()

        return jsonify([order.to_json() for order in orders])
    elif request.method == 'POST':
        data = request.get_json()
        order = Order(table_number=data['table_number'], items=data['items'], status='new')

        db.session.add(order)
        db.session.commit()

        return '', 201

@app.route('/orders/<int:order_id>', methods=['GET', 'PUT', 'DELETE'])
def order(order_id):
    if request.method == 'GET':
        order = Order.query.get(order_id)

        return jsonify(order.to_json())
    elif request.method == 'PUT':
        data = request.get_json()
        order = Order.query.get(order_id)

        order.table_number = data['table_number']
        order.items = data['items']
        order.status = data['status']

        db.session.commit()

        return '', 200
    elif request.method == 'DELETE':
        order = Order.query.get(order_id)

        db.session.delete(order)
        db.session.commit()

        return '', 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        order1 = Order(table_number=1, items='Item 1, Item 2', status='new')
        order2 = Order(table_number=2, items='Item 3, Item 4', status='new')

        db.session.add(order1)
        db.session.add(order2)
        db.session.commit()

    app.run()
