import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random,math
import threading

def initialise(self):
    # infura_url = "http://127.0.0.1:7545"
    # self.web3 = Web3(Web3.HTTPProvider(infura_url))
    # print(self.web3.isConnected())
    # print(self.web3.eth.blockNumber)
    # # f=open("../src/abis/PathFind.json")
    # f=open("../src/abis/PathFind.json")
    # data=json.load(f)
    # self.contract = self.web3.eth.contract(address=data["networks"]["5777"]["address"], abi=data["abi"])
    # f.close()
    #
    # check = self.contract.functions.transaction().call()
    # print(check)
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
    return self

class Simulator:
    def __init__(self):



        self=initialise(self)
        marker_style.update(markersize=300)
        x=self.ax.scatter3D([1],[1],[1],marker='$'+str(1)+'$',**marker_style, picker = True)
        plt.show()





Simulator()
