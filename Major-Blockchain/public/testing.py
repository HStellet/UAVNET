import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random,math
import threading
import json
import time
from web3 import Web3
import numpy as np

def initialise(self):
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

class Simulator:
    def __init__(self):

        self=initialise(self)
        x=self.ax.scatter3D([],[],[],marker='$'+str(6)+'$',s=300, c='blue', picker = True)
        print(x.get_properties())

Simulator()
