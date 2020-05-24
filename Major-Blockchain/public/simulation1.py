import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random,math
import threading
from dict import *
import json
import time
from web3 import Web3
from test1 import *
import numpy as np

def animatewa(self):
    self.anim = animation.FuncAnimation(self.fig,self.update,init_func=None,frames=4000,interval=10)
    plt.show()

def updateInfo(obj):
    while 1:
        for address,iot in dic.items():
            index=obj.contract.functions.getRegistered().call({'from':address})
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


# contract=None
def initialise(self):
    infura_url = "http://127.0.0.1:7545"
    self.web3 = Web3(Web3.HTTPProvider(infura_url))
    print(self.web3.isConnected())
    print(self.web3.eth.blockNumber)
    # f=open("../src/abis/PathFind.json")
    f=open("../src/abis/PathFind.json")
    data=json.load(f)
    self.contract = self.web3.eth.contract(address=data["networks"]["5777"]["address"], abi=data["abi"])
    f.close()

    check = self.contract.functions.transaction().call()
    print(check)
    self.fig = plt.figure()
    self.ax = self.fig.add_subplot(111, projection='3d')
    # Setting the axes properties
    self.ax.set_xlim3d([-9.0, 9.0])
    self.ax.set_xlabel('X')
    self.ax.set_ylim3d([-9.0, 9.0])
    self.ax.set_ylabel('Y')

    self.ax.set_zlim3d([-9.0, 9.0])
    self.ax.set_zlabel('Z')
    # f.close()
    self.data=dic
    return self

class Simulator:
    def __init__(self):



        self=initialise(self)
        # tz = threading.Thread(target=updateInfo,args=(self,), name='tz')
        # tz.start()
        t1 = threading.Thread(target=nodeProcess,args=(1,self), name='t1')
        t2 = threading.Thread(target=nodeProcess,args=(2,self), name='t2')
        t3 = threading.Thread(target=nodeProcess,args=(3,self), name='t3')
        t4 = threading.Thread(target=nodeProcess,args=(4,self), name='t4')
        t5 = threading.Thread(target=nodeProcess,args=(5,self), name='t5')
        t6 = threading.Thread(target=nodeProcess,args=(6,self), name='t6')
        t7 = threading.Thread(target=nodeProcess,args=(7,self), name='t7')
        t8 = threading.Thread(target=nodeProcess,args=(8,self), name='t8')
        t9 = threading.Thread(target=nodeProcess,args=(9,self), name='t9')


        t10 = threading.Thread(target=inputFn,args=(), name='t10')


        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t9.start()

        t10.start()
        t11 = threading.Thread(target=animatewa,args=(self,), name='t11')
        t11.start()


    def pointCreation(self):
        for address,iot in self.data.items():
            if len(iot)==7 and iot[4]==1:
                iot.append(self.ax.scatter3D([],[],[],marker='$'+str(iot[6])+'$',s=100, c='blue', picker = True))
            elif len(iot)==7 and iot[4]==0:
                iot.append(self.ax.scatter3D([],[],[],marker='$'+str(iot[6])+'$',s=100, c='#000000', picker = True))
            elif len(iot)==8 and iot[5]==0:
                self.data[address].pop()
            elif iot[5]==1 and iot[3]==1 and len(iot)==8:
                self.data[address][7]._facecolor3d[0]=[np.float64(1.0),np.float64(0.0),np.float64(0.0),np.float64(1.0)]
            elif iot[5]==1 and iot[3]==0 and len(iot)==8 and iot[4]==0:
                self.data[address][7]._facecolor3d[0]=[np.float64(0.0),np.float64(0.0),np.float64(0.0),np.float64(1.0)]


    def update(self,x):
        self.data=dic
        self.pointCreation()
        for key,value in self.data.items():
            p=(value[0],value[1],value[2])
            if len(self.data[key])==8:
                self.data[key][7]._offsets3d=[p[0]],[p[1]],[p[2]]



    def trajectory(self,coords,count):
        coords[0]+=self.data[count][6]/10
        coords[1]+=self.data[count][7]/10
        coords[2]+=self.data[count][8]/10

        # x=coords[0]
        # y=coords[1]
        # r=math.sqrt(coords[0]**2 + coords[1]**2 )
        # phi=1
        # if(x>0):
        #     phi+=math.degrees(math.atan(y/x))
        # elif(x<0 and y>0):
        #     phi+=180+math.degrees(math.atan(y/x))
        # elif(x<0 and y<0):
        #     phi+=-180+math.degrees(math.atan(y/x))
        # elif(x==0 and y>0):
        #     phi+=90
        # elif(x==0 and y<0):
        #     phi+=-90
        #
        # coords[0]=r*math.cos(math.radians(phi))
        # coords[1]=r*math.sin(math.radians(phi))

        # k=0.01
        # randInt=random.randint(0,7)
        # dicIntBin={
        #     0:[0,0,0],
        #     1:[0,0,1],
        #     2:[0,1,0],
        #     3:[0,1,1],
        #     4:[1,0,0],
        #     5:[1,0,1],
        #     6:[1,1,0],
        #     7:[1,1,1],
        #
        # }
        # for i in range(0,3):
        #     if count%2==1:
        #         if dicIntBin[randInt][i]==0:
        #             coords[i]+=k
        #         else:
        #             coords[i]+=k
        #     else:
        #         if dicIntBin[randInt][i]==0:
        #             coords[i]-=k
        #         else:
        #             coords[i]-=k

        return coords

    def axesUpdate(self,coords):
        self.ax.set_xlim3d([min(self.ax.get_xlim3d()[0],coords[0]),max(self.ax.get_xlim3d()[1],coords[0])])
        self.ax.set_ylim3d([min(self.ax.get_ylim3d()[0],coords[1]),max(self.ax.get_ylim3d()[1],coords[1])])
        self.ax.set_zlim3d([min(self.ax.get_zlim3d()[0],coords[2]),max(self.ax.get_zlim3d()[1],coords[2])])

Simulator()
