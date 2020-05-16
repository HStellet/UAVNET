import subprocess
import threading
def runFile(str):
    subprocess.run(["python3", str])

t1 = threading.Thread(target=runFile,args=("abc.py",), name='t1')
t2 = threading.Thread(target=runFile,args=("abc1.py",), name='t1')
t3 = threading.Thread(target=runFile,args=("server.py",), name='t1')
t1.start()
t2.start()
t3.start()
