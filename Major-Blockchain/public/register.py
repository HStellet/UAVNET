import json
import time
from web3 import Web3
import threading
from dict import *
from test1 import updateInfo
infura_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())
print(web3.eth.blockNumber)
f=open("../src/abis/PathFind.json")
data=json.load(f)
contract = web3.eth.contract(address=data["networks"]["5777"]["address"], abi=data["abi"])


address=dictAdd[str(10)]["address"]
# password=dictAdd[str(10)]["password"]
#
#
print(contract.functions.getRegistered().call({'from':address}))
#
# transaction = contract.functions.registration(dictAdd[str(10)]["pubkey"]).buildTransaction({
#     'from': address,
#     'value':web3.toWei(5,"ether"),
#     'nonce':web3.eth.getTransactionCount(address)
#
#     })
# private_key = password
#
# signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
# web3.eth.sendRawTransaction(signed_txn.rawTransaction)
#
# print(contract.functions.getRegistered().call({'from':address}))

# updateInfo(contract)
#
# print(contract.functions.getRegistered().call({'from':address}))
