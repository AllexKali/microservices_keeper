import unittest
from order.orders import app, db, Order

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_orders(self):
        response = self.app.get('/orders')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), [])

    def test_create_order(self):
        data = {
            'table_number': 1,
            'items': 'Item 1, Item 2'
        }
        response = self.app.post('/orders', json=data)
        self.assertEqual(response.status_code, 201)

        order = Order.query.first()
        self.assertEqual(order.table_number, data['table_number'])
        self.assertEqual(order.items, data['items'])
        self.assertEqual(order.status, 'new')

    def test_get_order(self):
        order = Order(table_number=1, items='Item 1, Item 2', status='new')
        db.session.add(order)
        db.session.commit()

        response = self.app.get(f'/orders/{order.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), order.to_json())

    def test_update_order(self):
        order = Order(table_number=1, items='Item 1, Item 2', status='new')
        db.session.add(order)
        db.session.commit()

        data = {
            'table_number': 2,
            'items': 'Item 3, Item 4',
            'status': 'completed'
        }
        response = self.app.put(f'/orders/{order.id}', json=data)
        self.assertEqual(response.status_code, 200)

        updated_order = Order.query.get(order.id)
        self.assertEqual(updated_order.table_number, data['table_number'])
        self.assertEqual(updated_order.items, data['items'])
        self.assertEqual(updated_order.status, data['status'])

    def test_delete_order(self):
        order = Order(table_number=1, items='Item 1, Item 2', status='new')
        db.session.add(order)
        db.session.commit()

        response = self.app.delete(f'/orders/{order.id}')
        self.assertEqual(response.status_code, 204)

        deleted_order = Order.query.get(order.id)
        self.assertIsNone(deleted_order)

if __name__ == '__main__':
    unittest.main()