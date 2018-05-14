# Author:zhouxy


# res =[i*2 for i in range(10)]
# print(res)

# a = (i*2 for i in range(10))
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())


# l=[1,2,3]
# i = l.__iter__()
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())


# def my_range(start,stop,step=1):
#     while start < stop:
#         yield start
#         start+=step
#
# #执行函数得到生成器，本质就是迭代器
# obj=my_range(1,7,2) #1  3  5
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj)) #StopIteration



# def fib(max):
#     n,a,b=0,0,1
#     while n <max:
#         yield b
#         a,b=b,a+b
#         n+=1
#     return 'done'
#
# data = fib(10)
# while True:
#     try:
#         k=next(data)
#         print(k)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break

# print(data.__next__())
# print(data.__next__())
# print(data.__next__())
# print(data.__next__())

# import time
# def consumer(name):  #消费者
#     print("%s 准备吃包子啦!" %name)
#     while True:
#        baozi = yield  #yield关键字的另外一种使用形式：表达式形式的yield
#        print("包子[%s]来了,被[%s]吃了!" %(baozi,name))
#
# def producer(name):  #生产者
#     c = consumer('A')
#     c2 = consumer('B') #迭代器
#     c.__next__()  #迭代器方法
#     c2.__next__()
#     print("老子开始准备做包子啦!")
#     for i in range(1,10):
#         time.sleep(1)
#         print("做了2个包子!")
#         c.send(i)
#
#
# producer('zhouxy')


def init(func):
    def wrapper(*args,**kwargs):
        g=func(*args,**kwargs)  # eater()
        next(g)
        return g
    return wrapper
@init  # eater=init(eater)
def eater(name):
    print('%s 准备开始吃饭啦' %name)
    food_list=[]
    while True:
        food=yield food_list
        print('%s 吃了 %s' % (name,food))
        food_list.append(food)

g=eater('egon') #wrapper()
g.send('蒸羊羔')



# def eater(name):
#     print('%s 准备开始吃饭啦' %name)
#     food_list=[]
#     while True:
#         food=yield food_list
#         print('%s 吃了 %s' % (name,food))
#         food_list.append(food)
#
# g=eater('zhouxy')
# g.send(None) #对于表达式形式的yield，在使用时，第一次必须传None，g.send(None)等同于next(g)
# g.send('蒸羊羔')
# g.send('蒸鹿茸')
# g.send('蒸熊掌')
# g.send('烧素鸭')
# g.send('烧素鹅')
# g.send('烧鹿尾')



