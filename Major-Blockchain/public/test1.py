from dict import *
import time
from web3 import Web3


def disseminate(data,contract,web3):
    transaction = contract.functions.send(data+data).buildTransaction({
        'from': address,
        'nonce':web3.eth.getTransactionCount(address),
        })
    private_key = password
    signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
    web3.eth.sendRawTransaction(signed_txn.rawTransaction)


def sendFunction(data,contract,web3):
    transaction = contract.functions.send(data).buildTransaction({
        'from': address,
        'nonce':web3.eth.getTransactionCount(address),
        })
    private_key = password
    signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
    web3.eth.sendRawTransaction(signed_txn.rawTransaction)

source=""
destination=""
uavNo=0
commandOption=0
def nodeProcess(port,contract,web3):
    global source
    global destination
    submitted=0
    timestamp
    Route=[]
    successful=False
    data=""
    address=dictAdd[str(port)]["address"]
    password=dictAdd[str(port)]["password"]
    while 1:
        global timestamp
        x=int(time.time())-timestamp
        value = contract.functions.transaction().call({'from':address})

        if value==False:
            submitted=0;
        if value==False and source==address:
            print(value,source)
            transaction = contract.functions.doTrans(destination).buildTransaction({
                'from': address,
                'nonce': web3.eth.getTransactionCount(address),
                })
            private_key = password
            signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
            web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            timestamp=time.time()
            print(timestamp)
        if value==True and submitted==0 and uavNo==port and commandOption==1:
            print(x,timestamp)

            transaction = contract.functions.registerCoordinates([2,0,0]).buildTransaction({
                'from': address,
                'value':web3.toWei(1,"ether"),
                'nonce':web3.eth.getTransactionCount(address)

                })
            private_key = password
            signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
            web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            submitted=1
        try:
            data=contract.functions.getData().call({'from':address})
        except:
            pass
        if data!="" and (address!=destination or address!=source) and value==True:
            print(x)

            input("Enter command Option for UAV "+str(port))
            if commandOption==2:
                sendFunction(data,contract,web3)
            elif commandOption==3:
                disseminate(data,contract,web3)
        elif data!="" and address==destination and x==40 and value==True:
            print(x)

            if decrypt(data,password=dictAdd[str(port)]["prikey"])==cloudServerData:
                transaction = contract.functions.success().buildTransaction({
                    'from': address,
                    'nonce':web3.eth.getTransactionCount(address),
                    })
                private_key = password
                signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
                web3.eth.sendRawTransaction(signed_txn.rawTransaction)
                source=""
                successful=True
            else:
                transaction = contract.functions.unsuccessful(1).buildTransaction({
                    'from': address,
                    'nonce':web3.eth.getTransactionCount(address),
                    })
                private_key = password
                signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
                web3.eth.sendRawTransaction(signed_txn.rawTransaction)
                transaction = contract.functions.returnCulprit().calll()
                print("Culprit",transaction)
                source=""
                destination=""
        elif data=="" and address==destination and x==40 and value==True:
            print(x)

            transaction = contract.functions.unsuccessful(0).buildTransaction({
                'from': address,
                'nonce':web3.eth.getTransactionCount(address),
                })
            private_key = password
            signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
            web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            source=""
            destination=""
        if value==True and address==source and x==8:
            print(x)
            transaction = contract.functions.updateGraph().buildTransaction({
                'from': address,
                'nonce':web3.eth.getTransactionCount(address),
                # 'gas':800000
                })
            private_key = password
            signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
            web3.eth.sendRawTransaction(signed_txn.rawTransaction)

            transaction = contract.functions.pathFind().buildTransaction({
                'from': address,
                'nonce':web3.eth.getTransactionCount(address),
                # 'gas':800000
                })
            private_key = password
            signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
            web3.eth.sendRawTransaction(signed_txn.rawTransaction)

            Route = (contract.functions.returnRoute().call())
            print(Route)
            transaction = contract.functions.send(cloudServerData).buildTransaction({
                'from': address,
                'nonce':web3.eth.getTransactionCount(address),
                })
            private_key = password
            signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
            web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        if successful==True and address==source:

            print(x)
            transaction = contract.functions.transCompleted().buildTransaction({
                'from': address,
                'nonce':web3.eth.getTransactionCount(address),
                'value':web3.toWei(len(Route)-2,"ether"),
                })
            private_key = password
            signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
            web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            destination=""
            successful=False

def inputFn():
    global source
    global destination
    global uavNo
    global commandOption
    while 1:
        if source=="" and destination=="":
            source,destination=input("Enter Source and destination").split(" ")
            source=dictAdd[source]["address"]
            destination=dictAdd[destination]["address"]
        print(source,destination)
        uavNo,commandOption=input("Uav and command").split(" ")
        uavNo=int(uavNo)
        commandOption=int(commandOption)
