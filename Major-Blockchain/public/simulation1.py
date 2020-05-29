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

    self.anim = animation.FuncAnimation(self.fig,self.update,init_func=None,frames=400000000,interval=4)
    plt.show()

def initiateBlockchain(self):
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

def initialise(self):
    try:
        initiateBlockchain(self)
        print("Blockchain connected")
    except:
        print("Blockchain couldn't connect")

    self.fig = plt.figure()
    self.ax = self.fig.add_subplot(111, projection='3d')
    # Setting the axes properties
    self.ax.set_xlim3d([0.0, 9.0])
    self.ax.set_xlabel('X')
    self.ax.set_ylim3d([0.0, 9.0])
    self.ax.set_ylabel('Y')

    self.ax.set_zlim3d([0.0, 9.0])
    self.ax.set_zlabel('Z')
    # f.close()
    return self

def showPlot(plt):
    plt.show()

class Simulator:
    def __init__(self):

        self=initialise(self)

        t1 = threading.Thread(target=nodeProcess,args=(1,self), name='t1')
        t2 = threading.Thread(target=nodeProcess,args=(2,self), name='t2')
        t3 = threading.Thread(target=nodeProcess,args=(3,self), name='t3')
        t4 = threading.Thread(target=nodeProcess,args=(4,self), name='t4')
        t5 = threading.Thread(target=nodeProcess,args=(5,self), name='t5')
        t6 = threading.Thread(target=nodeProcess,args=(6,self), name='t6')
        t7 = threading.Thread(target=nodeProcess,args=(7,self), name='t7')
        t8 = threading.Thread(target=nodeProcess,args=(8,self), name='t8')
        t9 = threading.Thread(target=nodeProcess,args=(9,self), name='t9')
        t11 = threading.Thread(target=animatewa,args=(self,), name='t11')
        t11.start()

        t10 = threading.Thread(target=updateInfo,args=(self,self.contract), name='t10')
        t10.start()
        #
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t9.start()

        # self.anim = animation.FuncAnimation(self.fig,self.update,init_func=None,frames=400000000,interval=6)
        # animatewa(self)
        # plt.show()


    def pointCreation(self):
        count=0
        for address,iot in dic.items():
            # index=self.contract.functions.getRegistered().call({'from':address})
            x=coordinates[address]
            if len(dic[address])==8:
                dic[address][7]._offsets3d=[x[0]],[x[1]],[x[2]]
                self.axesUpdate(address)
                if count>=3:
                    self.trajectory(address,count)
            count+=1
            if len(iot)==7 and iot[4]==1 and iot[5]!=0:
                iot.append(self.ax.scatter3D([],[],[],marker='$'+str(iot[6])+'$',s=300, c='blue', picker = True))
            elif len(iot)==7 and iot[4]==0 and iot[5]!=0:
                iot.append(self.ax.scatter3D([],[],[],marker='$'+str(iot[6])+'$',s=300, c='#000000', picker = True))
            elif len(iot)==8 and iot[5]==0:
                dic[address][7].remove()
                dic[address].pop()
            elif iot[5]==1 and iot[3]==1 and len(iot)==8:
                dic[address][7]._facecolor3d[0]=[np.float64(1.0),np.float64(0.0),np.float64(0.0),np.float64(1.0)]
            elif iot[5]==1 and iot[3]==0 and len(iot)==8 and iot[4]==0 and iot[7]._facecolor3d[0][0]==np.float64(1.0) and iot[7]._facecolor3d[0][1]==np.float64(0.0) and iot[7]._facecolor3d[0][2]==np.float64(0.0) and iot[7]._facecolor3d[0][3]==np.float64(1.0):
                dic[address][7]._facecolor3d[0]=[np.float64(0.0),np.float64(0.0),np.float64(0.0),np.float64(1.0)]


    def update(self,x):

        self.pointCreation()
        lineUpdate(self)

    def trajectory(self,key,count):

        x=coordinates[key][0]-5
        y=coordinates[key][1]-5

        r=math.sqrt(x**2 + y**2 )
        phi=0.8
        if count%2==0:
            if(x>0):
                phi+=math.degrees(math.atan(y/x))
            elif(x<0 and y>0):
                phi+=180+math.degrees(math.atan(y/x))
            elif(x<0 and y<0):
                phi+=-180+math.degrees(math.atan(y/x))
            elif(x==0 and y>0):
                phi+=90
            elif(x==0 and y<0):
                phi+=-90
            coordinates[key][0]=r*math.cos(math.radians(phi))+5
            coordinates[key][1]=r*math.sin(math.radians(phi))+5

        else:
            phi=-0.8
            if(x>0):
                phi+=math.degrees(math.atan(y/x))
            elif(x<0 and y>0):
                phi+=180+math.degrees(math.atan(y/x))
            elif(x<0 and y<0):
                phi+=-180+math.degrees(math.atan(y/x))
            elif(x==0 and y>0):
                phi+=90
            elif(x==0 and y<0):
                phi+=-90
            coordinates[key][0]=r*math.cos(math.radians(phi))+5
            coordinates[key][1]=r*math.sin(math.radians(phi))+5

    def axesUpdate(self,key):
        self.ax.set_xlim3d([min(self.ax.get_xlim3d()[0],coordinates[key][0]),max(self.ax.get_xlim3d()[1],coordinates[key][0])])
        self.ax.set_ylim3d([min(self.ax.get_ylim3d()[0],coordinates[key][1]),max(self.ax.get_ylim3d()[1],coordinates[key][1])])
        self.ax.set_zlim3d([min(self.ax.get_zlim3d()[0],coordinates[key][2]),max(self.ax.get_zlim3d()[1],coordinates[key][2])])


Simulator()
