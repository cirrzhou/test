# Author:zhouxy

# from multiprocessing import Process, Manager
# import os
#
# def f(d, l):
#     d[1] = '1'
#     d['2'] = 2
#     d[0.25] = None
#     l.append(os.getpid())
#     print(l)
#
# if __name__ == '__main__':
#     with Manager() as manager:
#         d = manager.dict()           #生成一个字典，可在多个进程间共享和传递
#         l = manager.list(range(5))   #生成一个列表，可在多个进程间共享和传递
#         p_list = []
#         for i in range(10):
#             p = Process(target=f, args=(d, l))
#             p.start()
#             p_list.append(p)
#         for res in p_list:
#             res.join()
#
#         print(d)
#         print(l)
# '''
# [0, 1, 2, 3, 4, 13220]
# [0, 1, 2, 3, 4, 13220, 9652]
# [0, 1, 2, 3, 4, 13220, 9652, 7400]
# [0, 1, 2, 3, 4, 13220, 9652, 7400, 14868]
# [0, 1, 2, 3, 4, 13220, 9652, 7400, 14868, 13348]
# [0, 1, 2, 3, 4, 13220, 9652, 7400, 14868, 13348, 2228]
# [0, 1, 2, 3, 4, 13220, 9652, 7400, 14868, 13348, 2228, 8312]
# [0, 1, 2, 3, 4, 13220, 9652, 7400, 14868, 13348, 2228, 8312, 15800]
# [0, 1, 2, 3, 4, 13220, 9652, 7400, 14868, 13348, 2228, 8312, 15800, 15868]
# [0, 1, 2, 3, 4, 13220, 9652, 7400, 14868, 13348, 2228, 8312, 15800, 15868, 18592]
# {1: '1', '2': 2, 0.25: None}
# [0, 1, 2, 3, 4, 13220, 9652, 7400, 14868, 13348, 2228, 8312, 15800, 15868, 18592]
# '''


from multiprocessing import Manager,Process,Lock
import os
def work(d,lock):
    # with lock: #不加锁而操作共享的数据,肯定会出现数据错乱
        d['count']-=1

if __name__ == '__main__':
    lock=Lock()
    with Manager() as m:
        dic=m.dict({'count':100})
        p_l=[]
        for i in range(10):
            p=Process(target=work,args=(dic,lock))
            p_l.append(p)
            p.start()
        for p in p_l:
            p.join()
        print(dic)
        #{'count': 90}