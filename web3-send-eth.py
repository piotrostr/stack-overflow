from web3 import Web3

def send_tx():
    from_address = ""
    w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
    tx = dict(
                nonce=w3.eth.getTransactionCount(),
                gasPrice=w3.eth.gasPrice,
                gas=100000,
                to=to_address,
                value=12345,
                data=b'',
            ),
                ,
            
    w3.eth.account.signTransaction(tx, private_key)
    w3.eth.send_transaction(tx)

if __name__ == '__main__':
