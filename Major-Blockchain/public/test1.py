from dict import *
import time
from web3 import Web3
import numpy as np

routeCount=0


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
    global value
    while 1:
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

    transaction = obj.contract.functions.send(data).buildTransaction({
        'from': address,
        'nonce':obj.web3.eth.getTransactionCount(address),
        })
    private_key = password

    signed_txn = obj.web3.eth.account.signTransaction(transaction, private_key=private_key)
    obj.web3.eth.sendRawTransaction(signed_txn.rawTransaction)

source=""
destination=""
value=False
value1=False
timestamp=0
successful=False
Route=[]
inputVar=0
source1=0
destination1=0

def nodeProcess(port,obj):
    global source1
    global destination1

    global routeCount
    global inputVar
    global source
    global destination
    global value
    global timestamp
    global successful
    global Route
    global value1
    submitted=0
    data=b''
    called=0
    # count=0
    cloudServerData="hello"
    address=dictAdd[str(port)]["address"]
    password=dictAdd[str(port)]["password"]
    while 1:
        if value1==False and inputVar==0 and source=="" and port==1:
            source1,destination1=input("Enter Source and destination").split(" ")
            source=dictAdd[source1]["address"]
            destination=dictAdd[destination1]["address"]
            inputVar=1
        x=int(time.time()-timestamp)
        value=obj.contract.functions.transaction().call({'from':address})

        if value==True and submitted==0 and port!=1 and port!=2 and port!=3:
            print(port,"has registered coordinates\n")
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

        if value==False:
            submitted=0
            called=0
        if value==False and source==address:
            print(source,destination)
            print("doTrans\n")

            transaction = obj.contract.functions.doTrans(destination).buildTransaction({
                'from': address,
                'nonce': obj.web3.eth.getTransactionCount(address),
                })
            private_key = password

            signed_txn = obj.web3.eth.account.signTransaction(transaction, private_key=private_key)
            obj.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            timestamp=time.time()
            value=True
            value1=True

        if len(Route)!=0 and routeCount>0 and Route[routeCount][0]==port:
            try:
                data=obj.contract.functions.getData().call({'from':address})
                # print("fetched",data,called,value,address,port)
            except:
                pass
        if called==0 and data!=b'' and (address!=destination and address!=source)  and value==True and len(Route)!=0 and routeCount<=len(Route)-1 and Route[routeCount][0]==port:
            print("DATA RECEIVED AT INTERMEDIATE NODE",str(port),": ",data,"\n")
            try:
                obj.line1.remove()
            except:
                pass
            called=1
            # if port==7:
            #     routeCount+=1
            #     disseminate(data,obj,address,password)
            # else:
            #     routeCount+=1
            #     sendFunction(data,obj,address,password)

            if port==4:
            # # drop()
                obj.line2, =obj.ax.plot([coordinates[address][0],coordinates[address][0]],[coordinates[address][1],coordinates[address][1]],[coordinates[address][2],coordinates[address][2]-3],color = '#000000',ls='--',marker='o')
                time.sleep(2)
                obj.line2.remove()
        elif data!=b'' and address==destination and x==27 and value==True:
            print("TIME: ",x)
            print("DATA RECEIVED AT DESTINATION: ",data,"\n")
            dataNew=""
            try:
                dataNew=decrypt(data,dictAdd[destination1]["prikey"]).decode()
            except:
                dataNew="error"
            print("DECRYPTED DATA: ",dataNew)

            if dataNew==cloudServerData:
                print("DATA MATCHED!\n")
                routeCount=0
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
                print("success\n")
                transaction = obj.contract.functions.success().buildTransaction({
                    'from': address,
                    'nonce':obj.web3.eth.getTransactionCount(address),
                    })
                private_key = password

                signed_txn = obj.web3.eth.account.signTransaction(transaction, private_key=private_key)
                obj.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
                destination=""
                destination1=0
                successful=True

                dic[address][7]._facecolor3d[0][0]=colorset[0]
                dic[address][7]._facecolor3d[0][1]=colorset[1]
                dic[address][7]._facecolor3d[0][2]=colorset[2]
                dic[address][7]._facecolor3d[0][3]=colorset[3]

            else:
                print("DATA MISMATCH!\n")

                try:
                    obj.line1.remove()
                except:
                    pass
                source=""
                destination=""
                source1=0
                destination1=0
                routeCount=0
                transaction = obj.contract.functions.unsuccessful(1).buildTransaction({
                    'from': address,
                    'nonce':obj.web3.eth.getTransactionCount(address),
                    })
                private_key = password

                signed_txn = obj.web3.eth.account.signTransaction(transaction, private_key=private_key)
                obj.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
                culpritX = obj.contract.functions.returnCulprit().call()
                print("Culprit",culpritX,"\n")


                transaction = obj.contract.functions.abort().buildTransaction({
                    'from': address,
                    'nonce':obj.web3.eth.getTransactionCount(address),
                    })
                private_key = password

                signed_txn = obj.web3.eth.account.signTransaction(transaction, private_key=private_key)
                obj.web3.eth.sendRawTransaction(signed_txn.rawTransaction)


                value=False
                print(culpritX,"blacklisted\n")
                called=0
                Route=[]
                data=b''
                inputVar=0
                value1=False
        elif data==b'' and address==destination and x==27 and value==True:
            try:
                obj.line1.remove()
            except:
                pass
            print("TIME:",x)
            print("NO DATA RECEIVED, MEANS IT HAS BEEN DROPPED\n")
            source=""
            destination=""
            source1=0
            destination1=0
            routeCount=0
            transaction = obj.contract.functions.unsuccessful(0).buildTransaction({
                'from': address,
                'nonce':obj.web3.eth.getTransactionCount(address),
                })
            private_key = password
            signed_txn = obj.web3.eth.account.signTransaction(transaction, private_key=private_key)
            obj.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            culpritX = obj.contract.functions.returnCulprit().call()
            print("Culprit",culpritX,"\n")
            transaction = obj.contract.functions.abort().buildTransaction({
                'from': address,
                'nonce':obj.web3.eth.getTransactionCount(address),
                })
            private_key = password

            signed_txn = obj.web3.eth.account.signTransaction(transaction, private_key=private_key)
            obj.web3.eth.sendRawTransaction(signed_txn.rawTransaction)

            value=False
            print(culpritX,"blacklisted","\n")
            data=b''
            called=0
            Route=[]
            inputVar=0
            value1=False

        if value==True and address==source and x==4:
            print("TIME: ",x,"\n")
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
            print(Route,"\n")
            if len(Route)==0:
                print("no path found\n")
                source=""
                destination=""
                successful=False
                value=False
                routeCount=0
                called=0
                Route=[]
                data=b''
                inputVar=0
                value1=False
            else:
                routeCount+=1
                data1=encrypt(cloudServerData,dictAdd[destination1]["pubkey"])
                print("DATA SENT FROM SOURCE: ",data1,"\n")
                sendFunction(data1,obj,address,password)
        if successful==True and address==source:
            source=""
            source1=0
            print("TIME: ",x,"transcompleted\n")
            transaction = obj.contract.functions.transCompleted().buildTransaction({
                'from': address,
                'nonce':obj.web3.eth.getTransactionCount(address),
                'value':obj.web3.toWei(len(Route)-2,"ether"),
                })
            private_key = password

            signed_txn = obj.web3.eth.account.signTransaction(transaction, private_key=private_key)
            obj.web3.eth.sendRawTransaction(signed_txn.rawTransaction)

            successful=False
            value=False
            routeCount=0
            called=0
            Route=[]
            data=b''
            inputVar=0
            value1=False
