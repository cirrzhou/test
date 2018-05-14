# Author:zhouxy
from multiprocessing import Pool
import os,time
def work(n):
    print('%s run' %os.getpid())
    time.sleep(1)
    return n**2

def Bar(arg):
    print('all done',arg)

if __name__ == '__main__':
    p=Pool(3) #进程池中从无到有创建三个进程,以后一直是这三个进程在执行任务
    res_l=[]
# 同步调用，直到本次任务执行完毕拿到res，等待任务work执行的过程中可能有阻塞也可能没有阻塞，但不管该任务是否存在阻塞，同步调用都会在原地等着，只是等的过程中若是任务发生了阻塞就会被夺走cpu的执行权限
    for i in range(10):
    #     res=p.apply(work,args=(i,))
    #     res_l.append(res)
    # print(res_l)
# 异步apply_async用法：如果使用异步提交的任务，主进程需要使用jion，等待进程池内任务都处理完，然后可以用get收集结果，否则，主进程结束，进程池可能还没来得及执行，也就跟着一起结束了
        res = p.apply_async(work, args=(i,),callback=Bar)  # callback 回调函数
        res_l.append(res)
    p.close() #关闭进程池，防止进一步操作。如果所有操作持续挂起，它们将在工作进程终止前完成
    p.join()  #调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    for res in res_l:
        print(res.get()) #使用get来获取apply_aync的结果,如果是apply,则没有get方法,因为apply是同步执行,立刻获取结果,也根本无需get