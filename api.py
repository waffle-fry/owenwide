from flask import Flask, jsonify
import owenwide

app = Flask(__name__)

# Health check endpoint


@app.route('/health')
def health():
    return jsonify(owenwide.health())

# Customers endpoint


@app.route('/customers')
def customers():
    return jsonify(owenwide.customers())

# Account balances endpoint


@app.route('/account_balances')
def account_balances():
    return jsonify(owenwide.account_balances())


if __name__ == '__main__':
    app.run(debug=True)
