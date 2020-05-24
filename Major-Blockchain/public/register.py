import json
import time
from web3 import Web3
import threading
from test1 import *
from dict import *

infura_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())
print(web3.eth.blockNumber)
f=open("../src/abis/PathFind.json")
data=json.load(f)
contract = web3.eth.contract(address=data["networks"]["5777"]["address"], abi=data["abi"])


#
# transaction = contract.functions.registerCoordinates([2,0,0]).buildTransaction({
#     'from': address,
#     'value':web3.toWei(4,"ether"),
#     'nonce':web3.eth.getTransactionCount(address)
#
#     })
# private_key = password
#
# signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
# web3.eth.sendRawTransaction(signed_txn.rawTransaction)
#
for i in range(1,10):
    address=dictAdd[str(i)]["address"]
    print(contract.functions.getRegistered().call({'from':address}))
# # #

# if contract.functions.getRegistered().call({'from':address})[0][0]=="0x0000000000000000000000000000000000000000":
#
#     if contract.functions.checkBlacklisted().call({'from':address})>10:
#         print("blacklisted node, can't register")
#     else:
#         password=dictAdd[str(9)]["password"]
#         contract = web3.eth.contract(address=data["networks"]["5777"]["address"], abi=data["abi"])
#         transaction = contract.functions.registration(dictAdd["9"]["pubkey"]).buildTransaction({
#             'from': address,
#             'value':web3.toWei(5,"ether"),
#             'nonce':web3.eth.getTransactionCount(address),
#             })
#         private_key = password
#
#         signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
#         web3.eth.sendRawTransaction(signed_txn.rawTransaction)
#
#
#         print(contract.functions.getRegistered().call({'from':address}))
# else:
#     print("already registered")
