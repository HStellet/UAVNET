

infura_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())
print(web3.eth.blockNumber)
f=open("../src/abis/PathFind.json")
data=json.load(f)

contract = web3.eth.contract(address=data["networks"]["5777"]["address"], abi=data["abi"])

check = contract.functions.transaction().call()
print(check)
# print(contract.functions.getData().call({'from':dictAdd["4"]["address"]}))
t1 = threading.Thread(target=nodeProcess,args=(1,contract,web3), name='t1')
t2 = threading.Thread(target=nodeProcess,args=(2,contract,web3), name='t2')
t3 = threading.Thread(target=nodeProcess,args=(3,contract,web3), name='t3')
t4 = threading.Thread(target=nodeProcess,args=(4,contract,web3), name='t4')
t5 = threading.Thread(target=nodeProcess,args=(5,contract,web3), name='t5')
t6 = threading.Thread(target=nodeProcess,args=(6,contract,web3), name='t6')
t7 = threading.Thread(target=nodeProcess,args=(7,contract,web3), name='t7')
t8 = threading.Thread(target=nodeProcess,args=(8,contract,web3), name='t8')
t9 = threading.Thread(target=inputFn,args=(), name='t9')


t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t9.start()
