import socket
import sys
import time
list=["0,0,-1","1,1,0","-1,1,0","-1,-1,0","1,-1,0","1,-1,0","-1,-1,0","-1,1,0","1,1,0","1,1,0","-1,1,0","-1,-1,0","1,-1,0","1,-1,0","-1,-1,0","-1,1,0","1,1,0","1,1,0","-1,1,0","-1,-1,0","1,-1,0","1,-1,0","-1,-1,0","-1,1,0","1,1,0","0,0,1","0,0,0"]

for str in list:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(('127.0.0.1', 12345)) #IP is the server IP

    s.send(bytes(str,encoding='ASCII'))
    time.sleep(1)

print('goodbye!')
