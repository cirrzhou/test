# Author:zhouxy
#
# import threading
# import time

# def sayhi(name): #定义每个线程要运行的函数
#     print('what is your name：%s'%name)
#     time.sleep(3)
#
# if __name__ == '__main__':
#
#     t1=threading.Thread(target=sayhi,args=('zhouxy',)) #生成一个线程实例
#     t2=threading.Thread(target=sayhi,args=('xyzhou',))
#
#     t1.start()#启动
#     t2.start()
#
#     print(t1.getName()) #获取线程名
#     print(t2.getName())


from threading import Thread
import time

# class Sayhi(Thread):
#
#     def __init__(self,name):
#         super().__init__() #threading.Thread.__init__(self)
#         self.name = name
#
#     def run(self):
#         print('what is your name:%s'%self.name)
#         time.sleep(3)
#
# start_time = time.time()
#
# if __name__ =='__main__':
#     for i in range (50):
#         t = Sayhi('t%s'%i)
#         t.start()
#     for i in range (50):
#         t = Sayhi('t%s'%i)
#         t.start()
#
# print('执行时间：',time.time()-start_time)


# import time
# import threading
#
# def run(n):
#     print('[%s]------running----\n' % n)
#     time.sleep(2)
#     print('--done--')
#
# def main():
#     for i in range(5):
#         t = threading.Thread(target=run, args=[i, ])
#         t.start()
#         t.join(1)
#         print('starting thread', t.getName())
#
# m = threading.Thread(target=main, args=[])
# m.setDaemon(True)  # 将main线程设置为Daemon线程,它做为程序主线程的守护线程,当主线程退出时,m线程也会退出,由m启动的其它子线程会同时退出,不管是否执行完任务
# m.start()
# m.join(timeout=2)
# print("---main thread done----")



# from threading import Thread
# import time
# def sayhi(name):
#     time.sleep(2)
#     print('%s say hello' %name)
#
# if __name__ == '__main__':
#     t=Thread(target=sayhi,args=('egon',))
#     t.start()
#     t.join()
#     print('主线程')
#     print(t.is_alive())
#     '''
#     egon say hello
#     主线程
#     False
#     '''

# from threading import Thread
# from multiprocessing import Process
# import os
#
# def work():
#     print('hello')
#
# if __name__ == '__main__':
#     #在主进程下开启线程
#     t=Thread(target=work)
#     t.start()
#     print('主线程/主进程')
#     '''
#     打印结果:
#     hello
#     主线程/主进程
#     '''
#
#     #在主进程下开启子进程
#     t=Process(target=work)
#     t.start()
#     print('主线程/主进程')
#     '''
#     打印结果:
#     主线程/主进程
#     hello
#     '''

# from threading import Thread
# from multiprocessing import Process
# import os
#
# def work():
#     print('hello',os.getpid())
#
# if __name__ == '__main__':
#     #part1:在主进程下开启多个线程,每个线程都跟主进程的pid一样
#     t1=Thread(target=work)
#     t2=Thread(target=work)
#     t1.start()
#     t2.start()
#     print('主线程/主进程pid',os.getpid())
#
#     #part2:开多个进程,每个进程都有不同的pid
#     p1=Process(target=work)
#     p2=Process(target=work)
#     p1.start()
#     p2.start()
#     print('主线程/主进程pid',os.getpid())

#主线程等待子线程结束
# from threading import Thread
# import time
# def Sayhi(name):
#     time.sleep(2)
#     print('%s say hello' %name)
#
# if __name__ == '__main__':
#     t=Thread(target=Sayhi,args=('zhouxy',))
#     t.start() #启动线程
#     t.join()
#     print('主线程')
#     print(t.is_alive()) #子线程是否活动
#     '''
#     zhouxy say hello
#     主线程
#     False
#     '''


# from threading import Thread
# import threading
# from multiprocessing import Process
# import os
#
# def work():
#     import time
#     time.sleep(10)
#     print(threading.current_thread().getName())
#
#
# if __name__ == '__main__':
#     #在主进程下开启线程
#     t=Thread(target=work)
#     t.start()
#
#     print(threading.current_thread().getName())
#     print(threading.current_thread()) #主线程
#     print(threading.enumerate()) #连同主线程在内有两个运行的线程
#     print(threading.active_count())
#     print('主线程/主进程')


# from threading import Thread
# import time
# def sayhi(name):
#     time.sleep(2)
#     print('%s say hello' %name)
#
# if __name__ == '__main__':
#     t=Thread(target=sayhi,args=('zhouxy',))
#     t.setDaemon(True) #必须在t.start()之前设置
#     t.start()
#
#     print('主线程')
#     print(t.is_alive())
#     '''
#     主线程
#     True
#     '''


import threading,os,time

def work():
    lock.acquire()
    global n
    temp=n
    time.sleep(0.1)
    n=temp-1
    lock.release()
if __name__ == '__main__':
    n=100
    l=[]  #存线程实例
    for i in range(100):
        p=Thread(target=work)
        l.append(p)   #为了不组赛后面线程的启动，不在这里join，先放到一个列表里
        p.start()
    for p in l: #循环线程实例列表，等待所有线程执行完毕
        p.join()

    print(n) #结果可能为99