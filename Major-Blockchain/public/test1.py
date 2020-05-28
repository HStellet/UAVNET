from dict import *
import time
from web3 import Web3
import numpy as np

routeCount=0
addressLine=""


def lineUpdate(obj):
    global routeCount

    if routeCount>0:
        try:
            obj.line1.set_xdata([coordinates[Route[routeCount-1][1]][0],coordinates[Route[routeCount][1]][0]])
            obj.line1.set_ydata([coordinates[Route[routeCount-1][1]][1],coordinates[Route[routeCount][1]][1]])
            obj.line1.set_3d_properties([coordinates[Route[routeCount-1][1]][2],coordinates[Route[routeCount][1]][2]])
        except:
            pass

def updateInfo(obj,contract):
    while 1:
        # lineUpdate(obj)
        for address,iot in dic.items():

            index=contract.functions.getRegistered().call({'from':address})
            # print(index)
            dic[address][6]=index[2]

            if index[2]!=0 and index[0][9]==0 and index[0][2]==0:
                dic[address][3]=0
                dic[address][4]=0
                dic[address][5]=1


            elif index[2]!=0 and index[0][9]==1 and index[0][2]==0:
                dic[address][3]=0
                dic[address][4]=1
                dic[address][5]=1

            elif index[2]==0:
                dic[address][5]=0


            elif index[2]!=0 and index[0][9]==1 and index[0][2]!=0:
                dic[address][3]=1
                dic[address][4]=1
                dic[address][5]=1
            elif index[2]!=0 and index[0][9]==0 and index[0][2]!=0:
                dic[address][3]=1
                dic[address][4]=0
                dic[address][5]=1


def disseminate(data,obj,address,password):
    obj.line1, =obj.ax.plot([],[],[],color = 'green',ls='--',marker='>')
    # lineUpdate(obj,address)
    transaction = obj.contract.functions.send(data+data).buildTransaction({
        'from': address,
        'nonce':obj.web3.eth.getTransactionCount(address),
        })
    private_key = password

    signed_txn = obj.web3.eth.account.signTransaction(transaction, private_key=private_key)
    obj.web3.eth.sendRawTransaction(signed_txn.rawTransaction)


def sendFunction(data,obj,address,password):
    obj.line1, =obj.ax.plot([],[],[],color = 'blue',ls='--',marker='>')
    # tz = threading.Thread(target=lineUpdate,args=(obj,), name='tz')
    # tz.start()

    # lineUpdate(obj,address)
    transaction = obj.contract.functions.send(data).buildTransaction({
        'from': address,
        'nonce':obj.web3.eth.getTransactionCount(address),
        })
    private_key = password

    signed_txn = obj.web3.eth.account.signTransaction(transaction, private_key=private_key)
    obj.web3.eth.sendRawTransaction(signed_txn.rawTransaction)

source=""
destination=""
uavNo=0
commandOption=0
value=False
timestamp=0
successful=False
Route=[]
inputVar=0

def nodeProcess(port,obj):
    global routeCount
    global inputVar
    global source
    global destination
    global uavNo
    global commandOption
    global value
    global timestamp
    global successful
    global Route
    submitted=0
    data=""
    called=0
    # count=0
    cloudServerData="hello"
    address=dictAdd[str(port)]["address"]
    password=dictAdd[str(port)]["password"]
    while 1:

        value=obj.contract.functions.transaction().call({'from':address})
        x=int(time.time()-timestamp)
        if value==True and submitted==0 and port!=1 and port!=2 and port!=3:
            print("registered coordinates")
            print([dic[address][0],dic[address][1],dic[address][2]])
            try:
                transaction = obj.contract.functions.registerCoordinates([dic[address][0],dic[address][1],dic[address][2]]).buildTransaction({
                    'from': address,
                    'value':obj.web3.toWei(1,"ether"),
                    'nonce':obj.web3.eth.getTransactionCount(address)

                    })
                private_key = password

                signed_txn = obj.web3.eth.account.signTransaction(transaction, private_key=private_key)
                obj.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            except:
                print(port, "can't register")
            submitted=1

        if value==False and port==1 and inputVar==0:
            source,destination=input("Enter Source and destination").split(" ")
            source=dictAdd[source]["address"]
            destination=dictAdd[destination]["address"]
            inputVar=1


        if value==False:
            submitted=0;
        if value==False and source==address:
            print(source,destination)
            print("doTrans")

            transaction = obj.contract.functions.doTrans(destination).buildTransaction({
                'from': address,
                'nonce': obj.web3.eth.getTransactionCount(address),
                })
            private_key = password

            signed_txn = obj.web3.eth.account.signTransaction(transaction, private_key=private_key)
            obj.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            timestamp=time.time()
            print(timestamp)
            value=True

        try:
            data=obj.contract.functions.getData().call({'from':address})
        except:
            pass
        if data!="" and (address!=destination and address!=source) and called==0 and value==True and len(Route)!=0 and Route[routeCount][0]==port:
            try:
                obj.line1.remove()
            except:
                pass
            print(address,destination)
            print("intermediate",str(port))
            called=1
            # if port==7:
            routeCount+=1
            sendFunction(data,obj,address,password)
            # else:
            #     routeCount+=1
            #     sendFunction(data,obj,address,password)

            # elif port==7:
            # # # drop()
            #     obj.line2, =obj.ax.plot([coordinates[address][0],coordinates[address][0]],[coordinates[address][1],coordinates[address][1]],[coordinates[address][2],coordinates[address][2]-3],color = '#000000',ls='--',marker='o')
            #     time.sleep(1)
            #     obj.line2.remove()
        elif data!="" and address==destination and x==30 and value==True:
            print(x,data)
            called=0
            if data==cloudServerData:
                try:
                    obj.line1.remove()
                except:
                    pass
                colorset=[]
                colorset.append(dic[address][7]._facecolor3d[0][0])
                colorset.append(dic[address][7]._facecolor3d[0][1])
                colorset.append(dic[address][7]._facecolor3d[0][2])
                colorset.append(dic[address][7]._facecolor3d[0][3])

                dic[destination][7]._facecolor3d[0]=[np.float64(0.17647059),np.float64(0.7254902),np.float64(0.01568627),np.float64(1.0)]
                print("success")
                transaction = obj.contract.functions.success().buildTransaction({
                    'from': address,
                    'nonce':obj.web3.eth.getTransactionCount(address),
                    })
                private_key = password

                signed_txn = obj.web3.eth.account.signTransaction(transaction, private_key=private_key)
                obj.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
                destination=""
                successful=True
                dic[address][7]._facecolor3d[0][0]=colorset[0]
                dic[address][7]._facecolor3d[0][1]=colorset[1]
                dic[address][7]._facecolor3d[0][2]=colorset[2]
                dic[address][7]._facecolor3d[0][3]=colorset[3]

            else:
                try:
                    obj.line1.remove()
                except:
                    pass
                print(disseminate)
                transaction = obj.contract.functions.unsuccessful(1).buildTransaction({
                    'from': address,
                    'nonce':obj.web3.eth.getTransactionCount(address),
                    })
                private_key = password

                signed_txn = obj.web3.eth.account.signTransaction(transaction, private_key=private_key)
                obj.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
                transaction = obj.contract.functions.returnCulprit().call()
                print("Culprit",transaction)


                transaction = obj.contract.functions.abort().buildTransaction({
                    'from': address,
                    'nonce':obj.web3.eth.getTransactionCount(address),
                    })
                private_key = password

                signed_txn = obj.web3.eth.account.signTransaction(transaction, private_key=private_key)
                obj.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
                source=""
                destination=""
                routeCount=0
                value=False
                print("blacklisted")
                inputVar=0


        elif data=="" and address==destination and x==30 and value==True:
            try:
                obj.line1.remove()
            except:
                pass
            print(x,data)
            called=0
            transaction = obj.contract.functions.unsuccessful(0).buildTransaction({
                'from': address,
                'nonce':obj.web3.eth.getTransactionCount(address),
                })
            private_key = password
            signed_txn = obj.web3.eth.account.signTransaction(transaction, private_key=private_key)
            obj.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            transaction = obj.contract.functions.returnCulprit().call()
            print("Culprit",transaction)
            transaction = obj.contract.functions.abort().buildTransaction({
                'from': address,
                'nonce':obj.web3.eth.getTransactionCount(address),
                })
            private_key = password

            signed_txn = obj.web3.eth.account.signTransaction(transaction, private_key=private_key)
            obj.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            source=""
            destination=""
            routeCount=0
            value=False

            print("blacklisted")
            inputVar=0


        if value==True and address==source and x==5:
            print(x)
            transaction = obj.contract.functions.updateGraph().buildTransaction({
                'from': address,
                'nonce':obj.web3.eth.getTransactionCount(address),
                # 'gas':800000
                })
            private_key = password

            signed_txn = obj.web3.eth.account.signTransaction(transaction, private_key=private_key)
            obj.web3.eth.sendRawTransaction(signed_txn.rawTransaction)

            transaction = obj.contract.functions.pathFind().buildTransaction({
                'from': address,
                'nonce':obj.web3.eth.getTransactionCount(address),
                # 'gas':800000
                })
            private_key = password

            signed_txn = obj.web3.eth.account.signTransaction(transaction, private_key=private_key)
            obj.web3.eth.sendRawTransaction(signed_txn.rawTransaction)

            Route = (obj.contract.functions.returnRoute().call())
            print(Route)
            if len(Route)==0:
                print("no path found")
                source=""
                destination=""
            else:
                routeCount+=1
                sendFunction(cloudServerData,obj,address,password)
        if successful==True and address==source:

            print(x,"transcompleted")
            transaction = obj.contract.functions.transCompleted().buildTransaction({
                'from': address,
                'nonce':obj.web3.eth.getTransactionCount(address),
                'value':obj.web3.toWei(len(Route)-2,"ether"),
                })
            private_key = password

            signed_txn = obj.web3.eth.account.signTransaction(transaction, private_key=private_key)
            obj.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            source=""
            successful=False
            value=False
            routeCount=0
            inputVar=0
        if uavNo==port and commandOption==4:
            print(uavNo,commandOption)
            transaction = obj.contract.functions.abort().buildTransaction({
                'from': address,
                'nonce':obj.web3.eth.getTransactionCount(address),
                })
            private_key = password

            signed_txn = obj.web3.eth.account.signTransaction(transaction, private_key=private_key)
            obj.web3.eth.sendRawTransaction(signed_txn.rawTransaction)

            destination=""
            source=""
            uavNo=0
            commandOption=0
