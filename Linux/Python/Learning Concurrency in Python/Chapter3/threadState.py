import threading 
import time

def threadWorker():
    print("My thread has enetered the 'Running' State")
    time.sleep(10)
    print("My thread is terminating")

myThread = threading.Thread(target = threadWorker)
myThread.start()
myThread.join()
print("My thread has entered a 'Dead' state")