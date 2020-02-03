import time
import os
from threading import Thread

class Task(Thread):
    'to execute multiple task by threads'

    def run(self):
        'to execute Thread task'
        tn = self.getName()
        if tn == "1st":
            self.loop(10000)
        elif tn == "2nd":
            self.copy("E://html/images/four.jpg","E://test/four/jpg")
        else:
            self.playTime(60)

    def loop(self,MAX):
        'to execute loop'
        for i in range(MAX+1):
            if i==MAX/2:
                raw_input("enter any key to continue : ")
            print("I : %d" %i)
        else:
            print("looping done")

    def playTime(self,Time):
        'to pass/consume given time'
        for i in range(Time+1):
            print("Time : %d second" %i)
            # hold/sleep execution for 1 second
            time.sleep(1)
        else:
            print("Time Completed")

    def copy(self, SFPATH, DFPATH):
        'to copy from 1 file & paste into 2nd file'
        #finding file size 
        FS = os.stat(SFPATH).st_size
        FR = open(SFPATH,"rb")
        FW = open(DFPATH,"wb")
        for i in range(FS):
            FW.write(FR.read())
            print("COPY : %0.2f KB " %(i/1024))
        else:
            FR.close()
            FW.close()
            print("copy paste done")
t1 = Task() 
t2 = Task()
t3 = Task()
t1.setName("1st")
t2.setName("2nd")
t3.setName("3rd")
t1.start()
t2.start()
t3.start()