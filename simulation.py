import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random,math
import numpy
import http.server
import socketserver


dic=[]

def getEquidistantPoints(p1, p2, parts):
    return zip(numpy.linspace(p1[0], p2[0], parts+1),
               numpy.linspace(p1[1], p2[1], parts+1),
               numpy.linspace(p1[2], p2[2],parts+1))

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
    dic.append(input_fn())
    dic.append(input_fn())

class Simulator:
    def __init__(self):

        simultaneousInput()
        self=initialise(self)
        self.anim = animation.FuncAnimation(self.fig,self.update,init_func=None,frames=40000,interval=10)
        plt.show()

    def pointCreation(self):
        count=0
        for uav in self.data:
            count+=1
            if len(uav)==5:
                uav.append(self.ax.scatter3D([],[],[],marker='$'+str(count)+'$',s=100, c='#000000', picker = True))

    def update(self,x):
        self.data=dic
        self.pointCreation()

        count=0
        for coords in self.data:
            count+=1
            p1=(coords[0],coords[1],coords[2])

            p2=tuple(self.trajectory([coords[0],coords[1],coords[2]]))
            # list1 = getEquidistantPoints(p1,p2,3)
            # for point in list1:
            self.axesUpdate(p1)

            self.data[count-1][-1]._offsets3d=[p1[0]],[p1[1]],[p1[2]]
            self.lineUpdate()
            self.data[count-1][0]=p2[0]
            self.data[count-1][1]=p2[1]
            self.data[count-1][2]=p2[2]

    def trajectory(self,coords):
        x=coords[0]
        y=coords[1]
        r=math.sqrt(coords[0]**2 + coords[1]**2 )
        phi=2
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

        coords[0]=r*math.cos(math.radians(phi))
        coords[1]=r*math.sin(math.radians(phi))
        # speed=random.randint(0,5)/50
        # time=1
        # k=random.uniform(0,(speed*time)/math.sqrt(3))
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
        #     if dicIntBin[randInt][i]==0:
        #         coords[i]+=k
        #     else:
        #         coords[i]+=k
        #
        return coords

    def axesUpdate(self,coords):
        self.ax.set_xlim3d([min(self.ax.get_xlim3d()[0],coords[0]),max(self.ax.get_xlim3d()[1],coords[0])])
        self.ax.set_ylim3d([min(self.ax.get_ylim3d()[0],coords[1]),max(self.ax.get_ylim3d()[1],coords[1])])
        self.ax.set_zlim3d([min(self.ax.get_zlim3d()[0],coords[2]),max(self.ax.get_zlim3d()[1],coords[2])])

    def lineUpdate(self):
        self.line1.set_xdata([self.data[0][0],self.data[1][0]])
        self.line1.set_ydata([self.data[0][1],self.data[1][1]])
        self.line1.set_3d_properties([self.data[0][2],self.data[1][2]])

        self.line2.set_xdata([self.data[2][0],self.data[1][0]])
        self.line2.set_ydata([self.data[2][1],self.data[1][1]])
        self.line2.set_3d_properties([self.data[2][2],self.data[1][2]])

Simulator()
