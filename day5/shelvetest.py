# Author:zhouxy

import shelve

d = shelve.open('shelve_test') #打开一个文件
name = ["zhouxy", "female", 18]
d["test"] = name  # 持久化列表
d['info']={'name':'zhouxy','age':18}
print(d.get('test'))
print(d.get('info'))
d.close()


