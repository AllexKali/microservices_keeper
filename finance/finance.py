from flask import Flask, request, jsonify
from datetime import datetime
import model

app = Flask(__name__)
@app.route('/transactions', methods=['POST'])
def create_transaction():
    data = request.json
    date = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    amount = data.get('amount')

    if amount is None:
        print(amount)
        return jsonify({'error': 'Invalid input'}), 400

    model.insert_transaction(date, amount)
    return jsonify({'message': 'Transaction created successfully'}), 201

@app.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = model.get_all_transactions()
    return jsonify(transactions), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5004)
