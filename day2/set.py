# Author:zhouxy
'''
list1 = [1,2,3,0,9,4,4,6,6,8,8]
list2 = [1,4,6,8]
list1 = set(list1)
list2 = set(list2)
print(list1,type(list1))  # 转为集合去重
print(list1.intersection(list2))  # 交集 like '&',使用运算符两个type都是set
print(list1.union(list2)) # 并集 like '|'
print(list1.difference(list2)) # 差集 in list1 but not in list2 like '-'
print(list1.symmetric_difference(list2)) # 对称差集 in list1 or in list2 but not both in list1 and list2 like '^'
print(list1.issubset(list2)) # list1是否为list2的子集 like '<='
print(list1.issuperset(list2)) # list1是否为list2的父集 like '>='
print(list1.isdisjoint(list2)) # 不存在交集返回为ture
'''
list1 = set([1,2,3,0,9,4,4,6,6,8,8])
list2 = set([1,4,6,8])
list2.add(2)   # 添加
list2.update([2,0,10]) # 添加多项
print(list2)
print(list1.remove(0)) # 指定存在元素删除
print(list1.pop()) # 随机删除元素并返回
print(list1.discard(10))  # 删除不存在元素不报错