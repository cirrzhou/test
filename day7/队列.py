# Author:zhouxy

# import queue
#
# q=queue.Queue(maxsize=2)
#
# q.put(1)
# q.put(2)
# q.put(block=False) #q.put(timeout=1)
#
# print(q.get())
# print(q.get())
# print(q.get(block=False)) # print(q.get(timeout=1))

# from multiprocessing import Process, Queue
#
# def f(qq):
#     qq.put([42, None, 'hello'])
#
# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=f, args=(q,)) #子进程
#     p.start()
#     print(q.get())  # prints "[42, None, 'hello']"
#     p.join()

from multiprocessing import Process
n=100 #在windows系统中应该把全局变量定义在if __name__ == '__main__'之上就可以了
def work():
    global n
    n=0
    print('子进程内: ',n)

if __name__ == '__main__':
    p=Process(target=work)
    p.start()
    print('主进程内: ',n)