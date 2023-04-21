def health():
    return {'status': 'ok'}


def customers():
    customers = [
        {'id': 1, 'name': 'John Doe'},
        {'id': 2, 'name': 'Jane Doe'},
        {'id': 3, 'name': 'Bob Smith'}
    ]

    return customers


def account_balances():
    account_balances = [
        {'id': 1, 'balance': 100.0},
        {'id': 2, 'balance': 500.0},
        {'id': 3, 'balance': 50.0}
    ]

    balances_dict = {}

    for balance in account_balances:
        balances_dict[balance['id']] = balance['balance']

    return balances_dict
