import json
import time
from web3 import Web3


infura_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())
print(web3.eth.blockNumber)
f=open("../src/abis/PathFind.json")
data=json.load(f)

contract = web3.eth.contract(address=data["networks"]["5777"]["address"], abi=data["abi"])

check = contract.functions.transaction().call()
print(check)
