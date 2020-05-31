import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random,math
import numpy
import socket
import threading

def create_socket(port):
    s = socket.socket()
    # print(type(s))
    print("Socket successfully created")
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', port))
    print("socket binded to %s" %(port))
    s.listen(5)
    print("socket is listening")

    while True:
       c, addr = s.accept()
       print('Got connection from', addr)
       buf1 = c.recv(128)
       list1=buf1.decode('ASCII').split(',')
       if port==8888:
           dic[0][6],dic[0][7],dic[0][8]=float(list1[0]),float(list1[1]),float(list1[2])
       elif port==12346:
           dic[1][6],dic[1][7],dic[1][8]=float(list1[0]),float(list1[1]),float(list1[2])
       elif port==12347:
           dic[2][6],dic[2][7],dic[2][8]=float(list1[0]),float(list1[1]),float(list1[2])

    s.close()

dic=[]



def initialise(self):
    self.fig = plt.figure()
    self.ax = self.fig.add_subplot(111, projection='3d')
    # Setting the axes properties
    self.ax.set_xlim3d([-7.0, 7.0])
    self.ax.set_xlabel('X')
    self.ax.set_ylim3d([-7.0, 7.0])
    self.ax.set_ylabel('Y')

    self.ax.set_zlim3d([-7.0, 7.0])
    self.ax.set_zlabel('Z')
    self.line1, =self.ax.plot([],[],[],color = 'blue',ls='--',marker='>')
    # self.line1.set_hatch('.')
    self.line2, =self.ax.plot([],[],[],color = 'red')
    return self

def input_fn():
    uav=input()
    uav=uav.split()
    uav[0]=int(uav[0])
    uav[1]=int(uav[1])
    uav[2]=int(uav[2])
    return list(uav)

def simultaneousInput():
    dic.append(input_fn())

    t1 = threading.Thread(target=create_socket,args=(8888,), name='t1')
    # t2 = threading.Thread(target=create_socket,args=(12346,), name='t2')
    # t3 = threading.Thread(target=create_socket,args=(12347,), name='t3')
    t1.start()
    # t2.start()
    # t3.start()


class Simulator:
    def __init__(self):

        simultaneousInput()
        self=initialise(self)
        self.anim = animation.FuncAnimation(self.fig,self.update,init_func=None,frames=4000,interval=5)
        plt.show()

    def pointCreation(self):
        count=0
        for uav in self.data:
            count+=1
            if len(uav)==5:
                uav.append(self.ax.scatter3D([],[],[],marker='$'+str(count)+'$',s=100, c='#000000', picker = True))
                uav.append(0)
                uav.append(0)
                uav.append(0)



    def update(self,x):
        self.data=dic
        self.pointCreation()
        # print(self.data)
        count=0
        for coords in self.data:
            count+=1
            p1=(coords[0],coords[1],coords[2])
            # print(p1)
            p2=tuple(self.trajectory([coords[0],coords[1],coords[2]],count-1))
            # list1 = getEquidistantPoints(p1,p2,3)
            # for point in list1:
            self.axesUpdate(p1)
            self.data[count-1][5]._offsets3d=[p1[0]],[p1[1]],[p1[2]]
            # self.lineUpdate()
            self.data[count-1][0]=p2[0]
            self.data[count-1][1]=p2[1]
            self.data[count-1][2]=p2[2]

    def trajectory(self,coords,count):
        coords[0]+=self.data[count][6]/10
        coords[1]+=self.data[count][7]/10
        coords[2]+=self.data[count][8]/10



        return coords

    def axesUpdate(self,coords):
        self.ax.set_xlim3d([min(self.ax.get_xlim3d()[0],coords[0]),max(self.ax.get_xlim3d()[1],coords[0])])
        self.ax.set_ylim3d([min(self.ax.get_ylim3d()[0],coords[1]),max(self.ax.get_ylim3d()[1],coords[1])])
        self.ax.set_zlim3d([min(self.ax.get_zlim3d()[0],coords[2]),max(self.ax.get_zlim3d()[1],coords[2])])

    # def lineUpdate(self):
    #     self.line1.set_xdata([self.data[0][0],self.data[1][0]])
    #     self.line1.set_ydata([self.data[0][1],self.data[1][1]])
    #     self.line1.set_3d_properties([self.data[0][2],self.data[1][2]])
    #
    #     self.line2.set_xdata([self.data[2][0],self.data[1][0]])
    #     self.line2.set_ydata([self.data[2][1],self.data[1][1]])
    #     self.line2.set_3d_properties([self.data[2][2],self.data[1][2]])


Simulator()
