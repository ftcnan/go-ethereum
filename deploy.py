import json
import web3
import time

from web3 import Web3
from web3.contract import ConciseContract
from web3.auto.gethdev import w3

abi = """[
    {
        "constant": false,
        "inputs": [],
        "name": "add",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "greeting",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "anonymous": false,
        "inputs": [],
        "name": "added",
        "type": "event"
    }
]"""

# web3.py instance

# set pre-funded account as sender
try:
    w3.personal.importRawKey("1" * 64, 'the-passphrase')
except:
    pass
w3.personal.unlockAccount(w3.eth.accounts[1], "the-passphrase")
w3.eth.defaultAccount = w3.eth.accounts[1]
w3.eth.sendTransaction({'to': w3.eth.accounts[1], 'from': w3.eth.accounts[0], 'value': 10 ** 70})

print("acct", w3.eth.accounts[1], "nonce", w3.eth.getTransactionCount(w3.eth.accounts[1]))
time.sleep(5)

# Instantiate and deploy contract
Greeter = w3.eth.contract(abi=abi, bytecode="60806040526000805534801561001457600080fd5b50610109806100246000396000f3006080604052600436106049576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff1680634f2be91f14605d578063ef690cc0146071575b348015605457600080fd5b50605b6099565b005b348015606857600080fd5b50606f6099565b005b348015607c57600080fd5b50608360d7565b6040518082815260200191505060405180910390f35b600160008082825401925050819055507fc87542064bc1930c362cb7f85a979ab1051627291e7db73dfda0f48bca40548160405160405180910390a1565b600054815600a165627a7a7230582076c969577f3ee624ab3870a450f66ea6e61f4d4e5160e0e2f51f8e43750484080029")

# Submit the transaction that deploys the contract
tx_hash = Greeter.constructor().transact()

# Wait for the transaction to be mined, and get the transaction receipt
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

#print(tx_receipt)
addr = tx_receipt.contractAddress
#print(w3.eth.getCode(addr))
print(addr)

# Create the contract instance with the newly-deployed address
greeter = w3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi,
)

# Display the default greeting from the contract


while True:
    tx_hash = greeter.functions.add().transact()

# Wait for transaction to be mined...
    rec = w3.eth.waitForTransactionReceipt(tx_hash)

    print(rec)
    time.sleep(5)

# Display the new greeting value
    print('Updated contract greeting: {}'.format(
        greeter.functions.greeting().call()
    ))
