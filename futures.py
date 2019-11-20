import json
import web3
import time

from web3 import Web3
from web3.contract import ConciseContract
from web3.auto.gethdev import w3

abi = """
 [{"constant": true,"inputs": [],"name": "numFuturesIssued","outputs": [{"name": "","type": "uint256"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": true,"inputs": [{"name": "","type": "uint256"},{"name": "","type": "uint256"}],"name": "ids","outputs": [{"name": "","type": "uint256"}],"payable": false,"stateMutability": "view","type": "function"},{"inputs": [{"name": "_token","type": "address"}],"payable": false,"stateMutability": "nonpayable","type": "constructor"},{"anonymous": false,"inputs": [{"indexed": true,"name": "id","type": "uint256"}],"name": "CreatedGasFuture","type": "event"},{"anonymous": false,"inputs": [{"indexed": false,"name": "id","type": "uint256"},{"indexed": false,"name": "price","type": "uint256"}],"name": "AuctionResult","type": "event"},{"constant": false,"inputs": [{"name": "_dex","type": "address"}],"name": "issue","outputs": [],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": false,"inputs": [{"name": "_id","type": "uint256"}],"name": "runAuction","outputs": [],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": false,"inputs": [],"name": "settle","outputs": [{"name": "","type": "bool"}],"payable": false,"stateMutability": "nonpayable","type": "function"}]
"""

# web3.py instance
# set pre-funded account as sender
w3.personal.unlockAccount(w3.eth.accounts[1], "password")
w3.eth.defaultAccount = w3.eth.accounts[1]


# Create the contract instance with the newly-deployed address
greeter = w3.eth.contract(
    address=Web3.toChecksumAddress("0x83bd509c95e724d3c0c1ec3561433611d81cc8df"),
    abi=abi
)

# Display the default greeting from the contract


while True:

# Display the new greeting value
    print('Futures outstanding: {}'.format(
        greeter.functions.numFuturesIssued().call()
    ))
    time.sleep(5)

