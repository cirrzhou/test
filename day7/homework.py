# Author:zhouxy

import threading,time
import queue

def Producer(name):
    count = 1
    while True:
        q.put(count)
        print('%s生产了%s个包子'%(name,count))
        time.sleep(0.2)

def Customer(name):
    while True:
        if q.qsize()>0:
            print('%s吃了%s个包子'%(name,q.get()))
            time.sleep(1)
        else:
            print('%s等待包子出笼'%name)
            time.sleep(0.1)

q = queue.Queue(maxsize=10)
t1 = threading.Thread(target=Producer,args=('zhouxy',))
t2 = threading.Thread(target=Customer,args='甲',)
t3 = threading.Thread(target=Customer,args='乙',)
t1.start()
t2.start()
t3.start()

