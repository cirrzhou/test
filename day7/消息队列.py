# Author:zhouxy


import queue

q=queue.Queue(maxsize=2)
q.put('first')
q.put('second')
print(q.get())
q.put('third')

print(q.qsize())
print(q.get())
print(q.get())
print(q.qsize())

'''
first
2
second
third
0
'''