from web3 import Web3
import json
from dict import *
infura_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(infura_url))


abi=json.loads('[{"constant":true,"inputs":[],"name":"get","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes","name":"y","type":"bytes"}],"name":"set","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
contract = web3.eth.contract(address="0xc421C7bD9C2b3A3965aB96C8EDa1E8CA8876F3b4", abi=abi)

x=encrypt("hello",dictAdd["1"]["pubkey"])

#
# y=contract.functions.get().call()
#
# print(y.decode('utf-8'))
# #
transaction = contract.functions.set(x).buildTransaction({
    'from': "0x660a5FB1d2a8f88aA2C89D473F43dF0b15eD718f",
    'nonce':web3.eth.getTransactionCount("0x660a5FB1d2a8f88aA2C89D473F43dF0b15eD718f"),
    })
private_key = "73d2fa7e4d3678f4b97ebd7e27e739380134e469eb6be4ced7099afa46003a80"

signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
web3.eth.sendRawTransaction(signed_txn.rawTransaction)
try:
    print(decrypt(contract.functions.get().call(),dictAdd["1"]["prikey"]).decode())
except:
    print("error")
