from web3 import Web3

Eth = "HTTP://127.0.0.1:8545"
w3 = Web3(Web3.HTTPProvider(Eth))

def get_blockchain_info():
    latest_block_number = w3.eth.blockNumber
    connection_status = w3.isConnected()
    latest_block = w3.eth.get_block('latest')
    return latest_block_number, connection_status, latest_block


print(get_blockchain_info())
print(" -------------------------------------------------------- ")
for data in get_blockchain_info():
    print(data)
