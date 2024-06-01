from flask import Flask, request, jsonify
from app import app
from transbank.webpay.webpay_plus.transaction import Transaction, WebpayOptions
from transbank.common.integration_type import IntegrationType

# Configura tus credenciales de Transbank
COMMERCE_CODE = '597055555532'
API_KEY = '579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C'
INTEGRATION_TYPE = IntegrationType.TEST

@app.route('/api/init_transaction', methods=['POST'])
def init_transaction():
    data = request.json
    amount = data.get('amount')
    buy_order = data.get('buy_order')
    session_id = data.get('session_id')
    return_url = data.get('return_url')

    options = WebpayOptions(
        commerce_code=COMMERCE_CODE,
        api_key=API_KEY,
        integration_type=INTEGRATION_TYPE
    )

    response = Transaction(options).create(buy_order, session_id, amount, return_url)
    return jsonify({
        'url': response['url'],
        'token': response['token']
    })

@app.route('/api/transaction_return', methods=['POST'])
def transaction_return():
    token = request.json.get('token_ws')

    options = WebpayOptions(
        commerce_code=COMMERCE_CODE,
        api_key=API_KEY,
        integration_type=INTEGRATION_TYPE
    )

    response = Transaction(options).commit(token)

    return jsonify({
        'status': response['status'],
        'amount': response['amount'],
        'authorization_code': response['authorization_code'],
        'transaction_date': response['transaction_date'],
        'buy_order': response['buy_order'],
        'card_detail': response['card_detail'],
        'accounting_date': response['accounting_date'],
        'session_id': response['session_id']
    })
