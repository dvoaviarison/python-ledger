# Install the package before run: 
# `pip3 install .`

import os
from pythonledger import SavingsAccount
from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)

# Configure swagger UI
template = {
  "swagger": "2.0",
  "info": {
    "title": "Python Ledger",
    "description": "Web API Sample using Python Ledger",
    "version": "0.0.1"
  },
  "basePath": "/"
}

swagger = Swagger(app, template=template)

# Create account
user = os.getlogin()
account = SavingsAccount()
account.create(1000)

# Update account using API
@app.route('/transactions', methods=['GET'])
def get_transactions():
    """Returns the list of all transactions
    ---
    responses:
      200:
        description: A list of all transactions
        examples:
          [{transaction_type: "Deposit", amount: 1000}]
    """
    return jsonify(transactions=[e.serialize() for e in account.transactions])

@app.route('/withdraw', methods=['POST'])
def withdraw():
    """Withdraws an amount from the account
    ---
    parameters:
        - name: amount
          in: query
          type: integer
          required: true
    responses:
      200:
        description: The account balance
    """
    amount = request.args.get('amount')
    account.withdraw(int(amount))
    return jsonify({"balance": account.balance})

@app.route('/deposit', methods=['POST'])
def deposit():
    """Deposits an amount from the account
    ---
    parameters:
        - name: amount
          in: query
          type: integer
          required: true
    responses:
      200:
        description: The account balance
    """
    amount = request.args.get('amount')
    account.deposit(int(amount))
    return jsonify({"balance": account.balance})

if __name__ == '__main__':
    app.run(debug=True)