import os
import shutil
import time 

T=time.time()
path = input("Enter the file path : ")
exist=os.path.exists(path)
desiredDays=input("Enter the desired day : ")

if exist==True :
    walk=os.walk(path)
    join=os.path.join(str(walk), "c-97/hello")
    ctime=os.stat(walk).st_ctime
    Time=T-ctime
    if Time > desiredDays :
        if os.path.isfile(walk):
            os.remove(walk)
        else:
            shutil.rmtree
elif exist==False:
    print("File not found")
print(exist)
