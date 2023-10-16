from flask import Flask, render_template, request
from web3 import Web3

app = Flask(__name__)
Eth = "HTTP://127.0.0.1:8545"
w3 = Web3(Web3.HTTPProvider(Eth))


def get_blockchain_info():
    latest_block_number = w3.eth.block_number
    connection_status = w3.is_connected()
    latest_block = w3.eth.get_block('latest')

    return latest_block_number, connection_status, latest_block


def get_latest_transaction_info(input_text):
    transaction = w3.eth.get_transaction(input_text)
    return transaction


@app.route('/')
def index():
    latest_block_number, connection_status, latest_block = get_blockchain_info()
    return render_template('index.html', block=latest_block_number, connection=connection_status,
                           latest_block=latest_block)


@app.route('/process_form', methods=['POST'])
def process_form():
    input_text = request.form.get('inputField')
    input_text = str(input_text)
    print(input_text)
    transaction = get_latest_transaction_info(input_text)
    print(transaction)
    latest_block_number, connection_status, latest_block = get_blockchain_info()
    return render_template('index.html', input=transaction, block=latest_block_number, connection=connection_status,
                           latest_block=latest_block)


if __name__ == '__main__':
    app.run(debug=True)
