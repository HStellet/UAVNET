from dict import *
import time
from web3 import Web3

def disseminate(data,contract,web3,address,password):
    transaction = contract.functions.send(data+data).buildTransaction({
        'from': address,
        'nonce':web3.eth.getTransactionCount(address),
        })
    private_key = password

    signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
    web3.eth.sendRawTransaction(signed_txn.rawTransaction)


def sendFunction(data,contract,web3,address,password):
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
value=False
timestamp=0
successful=False

def inputFn():
    global uavNo
    global commandOption
    while 1:
        if value==True:
            uavNo,commandOption=input("UAV and commandOption").split(" ")
            uavNo=int(uavNo)
            commandOption=int(commandOption)

def nodeProcess(port,contract,web3):
    global source
    global destination
    global uavNo
    global commandOption
    global value
    global timestamp
    global successful
    submitted=0
    Route=[]
    data=""
    called=0
    # count=0
    cloudServerData="hello"
    address=dictAdd[str(port)]["address"]
    password=dictAdd[str(port)]["password"]
    while 1:
        value=contract.functions.transaction().call({'from':address})
        x=int(time.time()-timestamp)
        # count+=1
        # # if(port==6 and count==1):
        # print(port)
        if value==True and submitted==0 and port==5:
            print("registered coordinates")

            transaction = contract.functions.registerCoordinates([2,0,0]).buildTransaction({
                'from': address,
                'value':web3.toWei(1,"ether"),
                'nonce':web3.eth.getTransactionCount(address)

                })
            private_key = password

            signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
            web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            submitted=1
        if value==True and submitted==0 and port==6:
            print("registered coordinates")

            transaction = contract.functions.registerCoordinates([2,2,0]).buildTransaction({
                'from': address,
                'value':web3.toWei(1,"ether"),
                'nonce':web3.eth.getTransactionCount(address)

                })
            private_key = password

            signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
            web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            submitted=1
        if value==False and port==1:
            source,destination=input("Enter Source and destination").split(" ")
            source=dictAdd[source]["address"]
            destination=dictAdd[destination]["address"]

        if value==False:
            submitted=0;
        if value==False and source==address:
            print("doTrans")

            transaction = contract.functions.doTrans(destination).buildTransaction({
                'from': address,
                'nonce': web3.eth.getTransactionCount(address),
                })
            private_key = password

            signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
            web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            timestamp=time.time()
            print(timestamp)
            value=True

        try:
            data=contract.functions.getData().call({'from':address})
        except:
            pass
        if data!="" and (address!=destination and address!=source) and value==True and called==0:
            print(address,destination)
            print("intermediate",str(port))
            called=1
            disseminate(data,contract,web3,address,password)
        elif data!="" and address==destination and x==30 and value==True:
            print(x,data)

            if data==cloudServerData:
                print("success")
                transaction = contract.functions.success().buildTransaction({
                    'from': address,
                    'nonce':web3.eth.getTransactionCount(address),
                    })
                private_key = password

                signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
                web3.eth.sendRawTransaction(signed_txn.rawTransaction)
                destination=""
                successful=True
            else:
                print(disseminate)
                transaction = contract.functions.unsuccessful(1).buildTransaction({
                    'from': address,
                    'nonce':web3.eth.getTransactionCount(address),
                    })
                private_key = password

                signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
                web3.eth.sendRawTransaction(signed_txn.rawTransaction)
                transaction = contract.functions.returnCulprit().call()
                print("Culprit",transaction)


                transaction = contract.functions.abort().buildTransaction({
                    'from': address,
                    'nonce':web3.eth.getTransactionCount(address),
                    })
                private_key = password

                signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
                web3.eth.sendRawTransaction(signed_txn.rawTransaction)
                source=""
                destination=""
                print("blacklisted")

        elif data=="" and address==destination and x==30 and value==True:
            print(x,data)

            transaction = contract.functions.unsuccessful(0).buildTransaction({
                'from': address,
                'nonce':web3.eth.getTransactionCount(address),
                })
            private_key = password
            signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
            web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            transaction = contract.functions.returnCulprit().call()
            print("Culprit",transaction)
            transaction = contract.functions.abort().buildTransaction({
                'from': address,
                'nonce':web3.eth.getTransactionCount(address),
                })
            private_key = password

            signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
            web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            source=""
            destination=""
            print("blacklisted")
        if value==True and address==source and x==10:
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
            if len(Route)==0:
                print("no path found")
                source=""
                destination=""
            else:
                transaction = contract.functions.send(cloudServerData).buildTransaction({
                    'from': address,
                    'nonce':web3.eth.getTransactionCount(address),
                    })
                private_key = password

                signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
                web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        if successful==True and address==source:

            print(x,"transcompleted")
            transaction = contract.functions.transCompleted().buildTransaction({
                'from': address,
                'nonce':web3.eth.getTransactionCount(address),
                'value':web3.toWei(len(Route)-2,"ether"),
                })
            private_key = password

            signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
            web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            source=""
            successful=False
        if uavNo==port and commandOption==4:
            print(uavNo,commandOption)
            transaction = contract.functions.abort().buildTransaction({
                'from': address,
                'nonce':web3.eth.getTransactionCount(address),
                })
            private_key = password

            signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
            web3.eth.sendRawTransaction(signed_txn.rawTransaction)

            destination=""
            source=""
            uavNo=0
            commandOption=0
